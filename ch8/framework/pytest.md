## pytest


* pip install pytest 로 설치한다.
* unittest 처럼 클래스 중심으로 테스트 하는 것이 가능하지만 필수는 아니고, 단순히 assert 구문을 사용해 검사가 가능하다.
* pytest 명령어를 통해 모든 테스트를 한번에 수행하는 것이 가능하다.


``` python
def test_simple_rejected():
    merge_request = MergeRequest()
    merge_request.downvote("maintainer")
    assert merge_request.status == MergeRequestStatus.REJECTED

def test_just_created_is_pending():
    assert MergeRequest().status == MergeRequestStatus.PENDING

def test_pending_awaiting_review():
    merge_request = MergeRequest()
    merge_request.upvote("core-dev")
    assert merge_request.status == MergeRequestStatus.PENDING
```
* 간단한 비교는 assert 구문만 사용하면 된다.
* 예외 검사
  ``` python
  def test_invalid_types():
      merge_request = MergeRequest()
      pytest.raises(TypeError, merge_request.upvote, {"invalid-object"})

  def test_cannot_vote_on_closed_merge_request():
      merge_request = MergeRequest()
      merge_request.close()
      pytest.raises(MergeRequestException, merge_request.upvote, "dev1")
      with pytest.raises(
          MergeRequestException, match="CLOSED 상태에서는 머지 요구를 할 수 없습니다."
      ):
          merge_request.downvote("dev1")
  ```


#### 테스트 파라미터화

* pytest를 활용하면 @pytest.mark.parametrize 데코레이터를 사용한다.

``` python
@pytest.mark.parametrize(
    "context,expected_status",
    (
        (
            {"downvotes": set(), "upvotes": set()}, 
            MergeRequestStatus.PENDING
        ),
        (
            {"downvotes": set(), "upvotes": {"dev1"}},
            MergeRequestStatus.PENDING,
        ),
        (
            {"downvotes": "dev1", "upvotes": set()}, 
            MergeRequestStatus.REJECTED
        ),
        (
            {"downvotes": set(), "upvotes": {"dev1", "dev2"}},
            MergeRequestStatus.APPROVED,
        ),
    ),
)
def test_acceptance_threshold_status_resolution(context, expected_status):
    assert AcceptanceThreshold(context).status() == expected_status

```



### 픽스쳐 (Fixture)

* pytest 는 테스트 코드의 재활용을 지원하는 기능이 강력하다.
* MergeRequest 객체는 여러 테스트에서 재사용하기 때문에 @pytest.fixture 데코레이터를 활용해 테스트시 픽스쳐 에서 전달한 객체를 재활용할 수 있다. 

``` python

@pytest.fixture
def rejected_mr():
    merge_request = MergeRequest()

    merge_request.downvote("dev1")
    merge_request.upvote("dev2")
    merge_request.upvote("dev3")
    merge_request.downvote("dev4")

    return merge_request


def test_simple_rejected(rejected_mr):
    assert rejected_mr.status == MergeRequestStatus.REJECTED


def test_rejected_with_approvals(rejected_mr):
    rejected_mr.upvote("dev2")
    rejected_mr.upvote("dev3")
    assert rejected_mr.status == MergeRequestStatus.REJECTED


def test_rejected_to_pending(rejected_mr):
    rejected_mr.upvote("dev1")
    assert rejected_mr.status == MergeRequestStatus.PENDING


def test_rejected_to_approved(rejected_mr):
    rejected_mr.upvote("dev1")
    rejected_mr.upvote("dev2")
    assert rejected_mr.status == MergeRequestStatus.APPROVED
```

* 픽스처는 테스트 스위트에서 자주 사용될 객체를 생성해서 재사용하는 것 이외에도 
* <font color="red">직접 호출되지 않은 함수를 수정하거나 사용될 객체를 미리 설정하는 등의 사전 조건 설정에도 사용된다.</font>


## 그 밖에

* pytest 는 기본적으로 현재 디렉토리의 모든 test_*.py 클래스나 *_test.py 를 찾아서 실행한다.
* 하위 경로를 주면 하위 경로의 테스트 클래스들을 찾아서 실행한다. 두개 이상을 줄 수도 있다.
* 테스트 클래스에는 __init__ 메쏘드가 있으면 안된다.
* 테스트 클래스의 메쏘드나 함수는 test_로 시작해야 한다.
* @pytest.mark 는 클래스를 선별해서 테스트 할 수 있게 해준다.
  


## 참고 
* [pytest 커스텀 마커 사용하기](http://doc.pytest.org/en/latest/example/markers.html)