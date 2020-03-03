
#### unittest
 * unittest는 python 의 기본 테스트 툴로 풍부한 API를 제공한다.
 * java의 JUnit을 모델로 만들어 졌다.
 * 테스트는 객체를 사용해 작성되며 클래스의 시나리오별로 테스트를 그룹화 하는 것이 일반적이다.
 * 테스트 클래스는 unittest.TestCase를 상속해서 만들어야 한다.
 * 테스트 메쏘드는 반드시 test_로 시작해야한다.(관례)

``` python
class TestMergeRequestStatus(unittest.TestCase):

    def test_1_단순_거절(self):
        merge_request = MergeRequest()
        merge_request.downvote("maintainer")
        self.assertEqual(
            merge_request.status,
            MergeRequestStatus.REJECTED
        )

    def test_2_이제막_생성된_건(self):
        self.assertEqual(
            MergeRequeest().status,
            MergeRequestStatus.PENDING
        )

    def test_3_검토대기(self):
        merge_request = MergeRequest()
        merge_request.upvote("core-dev")
        self.assertEqual(
            merge_request.status,
            MergeRequestStatus.PENDING
        )

    def test_4_승인(self):
        merge_request = MergeRequest()
        merge_request.upvote("dev1")
        merge_request.upvote("dev2")
        self.assertEqual(
            merge_request.status,
            MergeRequestStatus.APPROVED
        )
```

* 가장 많이 사용하는 비교 메쏘드는 TestCase의 assertEqual 이다.(assertEquals는 deprecate 되었음)
* 예외가 발생하면 예외를 던지고 호출자에게 바로 알려주는 것이 좋다. 예외 여부도 테스트의 대상이 된다.


#### 머지 리퀘스트 종료하기

머지 상황을 종료하는 상태를 하나 더 둔다. 머지를 종료하면 더 이상 투표를 할 수 없다.

``` python

class MergeRequest(object):
    """  merge 요구를 추상화한 엔터티 """

    def __init__(self):
        self._context = {
            "찬성": set(),
            "반대": set()
        }
        self._status = MergeRequestStatus.OPEN

    def close(self):
        self._status = MergeRequestStatus.CLOSED

    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestStatus.CLOSED:
            raise MergeRequestException("CLOSED 상태에서는 머지 요구를 할 수 없습니다.")

    def upvote(self, by_user:str):
        self._cannot_vote_if_closed()
        self._context["반대"].discard(by_user)
        self._context["찬성"].add(by_user)

    def downvote(self, by_user:str):
        self._cannot_vote_if_closed()
        self._context["찬성"].discard(by_user)
        self._context["반대"].add(by_user)
```

* 위 코드에 예외가 발생하므로 assertRaises와 assertRasisesRegex 메쏘드를 사용해 검증한다.
``` python
    
    def test_확장_머지가_종료된_요청에_찬성할_수_없음(self):
        self.merge_request.close()
        self.assertRaises(
            MergeRequestException, self.merge_request.upvote, "dev1"
        )

    def test_확장_머지가_종료된_요청에_반대할_수_없음(self):
        self.merge_request.close()
        self.assertRaisesRegex(
            MergeRequestException,
            "CLOSED 상태에서는 머지 요구를 할 수 없습니다.",
            self.merge_request.downvote,
            "dev1",
        )

```
* test_확장_머지가_종료된_요청에_찬성할_수_없음 : 실제 예외가 발생했는지 확인
* test_확장_머지가_종료된_요청에_반대할_수_없음 : 예외 메시지를 정규 표현식으로 확인


``` python
예외가 발생하는지 뿐만 아니라 오류 메시지도 확인하자. 
발생한 예외가 정확히 우리가 원했던 예외인지 확인해야 한다.
우연히 예상했던 것과 다른 이유로 같은 오류가 발생할 수도 있다.
```

#### 테스트 파라미터화

* 여러가지 테스트 케이스를 적용하기 위해서는 반드시 코드 중복이 발생하게 된다.
* 이를 최소화 하기 위해서 테스트 클래스를 좀 더 추상화 할 필요가 있다.

``` python
class AcceptanceThreshold:

    def __init__(self, merge_req_context: dict) -> None:
        self._context = merge_req_context

    def status(self):
        if self._context["반대"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["찬성"]) >= 2:
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING


class MergeRequest(object):
    ...
    @property
    def status(self):
        if self._status == MergeRequestStatus.CLOSED:
            return self._status
        return AcceptanceThreshold(self._context).status()
```

* 수정 후에도 기존 테스트는 잘 수행되어야 한다.
* 이후 테스트 케이스를 객체화해서 테스트를 수행할 수 있다.

``` python
# TestsUTFrameworks3(BaseCase, ExtendedCases, TestCase):

class TestAcceptanceThreshold  
    def setUp(self):
        self.fixture_data = (
            (
                {"반대": set(), "찬성": set()},
                MergeRequestStatus.PENDING,
            ),
            (
                {"반대": set(), "찬성": {"dev1"}},
                MergeRequestStatus.PENDING,
            ),
            (
                {"반대": "dev1", "찬성": set()},
                MergeRequestStatus.REJECTED,
            ),
            (
                {"반대": set(), "찬성": {"dev1", "dev2"}},
                MergeRequestStatus.APPROVED,
            ),
        )

    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status.value, expected.value)

```
* 코드를 이렇게 수정하면 파라미터를 쉽게 작성하여 다양한 테스트를 수행할 수 있다.
* subTest 핼퍼 메쏘드를 사용하고 있다. 실패시 적절한 메시지를 제공한다.

