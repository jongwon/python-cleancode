## Mock 객체


* 의존성이 있는 코드를 테스트할 때 mock 테스트를 진행한다.
* Mock 객체는 유용하지만 남용하면 냄새나는 나쁜 코드를 양산할 수 있으니 주의해야 한다.


### 패치와 모의에 대한 주의 사항


### Mock 객체 사용하기


### Mock 객체의 종류

* unittest.mock 모듈에서 다음 객체를 사용한다.
  * Mock 
    * 어떤 값도 반환 가능하다.
    * 모든 호출을 추적할 수 있다.
  * MagicMock 
    * 그 밖에 추가 매직 메써드를 제공한다.
  
``` python
class GitBranch:
    def __init__(self, commits: List[Dict]):
        self._commits = {c["id"]: c for c in commits}

    def __getitem__(self, commit_id):
        return self._commits[commit_id]

    def __len__(self):
        return len(self._commits)


def author_by_id(commit_id, branch):
    return branch[commit_id]["author"]

```

author_by_id 함수를 테스트 해보자.

``` python
def test_find_commit():
    branch = GitBranch([{"id": "123", "author": "dev1"}])
    assert author_by_id("123", branch) == "dev1"

def test_find_any():
    author = author_by_id("123", Mock()) is not None
```

MagicMock 객체를 사용해서 리턴값을 강제한 다음 아래와 같이 테스트 하면 테스트가 성공한다. 


``` python
def test_find_any():
    mbranch = MagicMock()
    mbranch.__getitem__.return_value = {"author": "test"}
    assert author_by_id("123", mbranch) == "test"
```
* 솔직히 이런 테스트 코드가 의미가 있을까??? 프로세스의 낭비 아닐까? 이런 생각을 하기 시작하면 단위 테스트 못한다. (제 생각)


#### testable 의 사용 예

* CI 툴에서 머지 요구의 빌드 상태를 표시하는 컴포넌트에 대한 테스트이다.
* 빌드가 끝나면 머지 요청에 따른 테스트 결과를 알린다.

``` python
class BuildStatus:

    @staticmethod
    def build_date() -> str:
        return datetime.utcnow().isoformat()

    @classmethod
    def notify(cls, merge_request_id, status):
        build_status = {
            "id": merge_request_id,
            "status": status,
            "built_at": cls.build_date(),
        }
        response = requests.post(STATUS_ENDPOINT, json=build_status)
        response.raise_for_status()
        return response
```
* 이 코드는 외부 모듈에 의존한다.
* 이 코드를 테스트 하려면 Mock 객체가 필요하다.

``` python
from unittest import mock
from unittest.mock import MagicMock

from ch8.constants import STATUS_ENDPOINT
from ch8.mock.mock_2 import BuildStatus


@mock.patch("mock_2.requests")
def test_build_notification_sent(mock_requests):
    build_date = "2020-01-01T00:00:01"
    with mock.patch("mock_2.BuildStatus.build_date", return_value=build_date):
        BuildStatus.notify(123, "OK")

    expected_payload = {"id": 123, "status": "OK", "built_at": build_date}
    mock_requests.post.assert_called_with(
        STATUS_ENDPOINT, json=expected_payload
    )

```

* mock_requests 라는 객체가 


