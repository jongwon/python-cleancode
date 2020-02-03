[위로](./summary.md)

## 1. 단일 책임 원칙 (SRP)

* 하나의 컴포넌트(클래스)는 하나의 일에 대해서만 책임져야 한다.
* 잘못 설계된 컴포넌트는 너무 많은 책임을 하나의 컴포넌트(god 객체?)에 맡긴다.
* 응집력 있는 추상화(유닉스 철학)
* 클래스의 메쏘드는 상호 배타적이며 서로 관련이 없어야 한다.

### 너무 많은 책임을 가진 클래스

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/1_srp_1.png" width="180" />
</div>

* 로그파일이나 데이터베이스에서 이벤트 정보를 읽어서 로그 별로 필요한 액션을 분류하는 클래스
* 개략적인 코드

``` python
# srp_1.py
class SystemMonitor:

  def load_activity(self):
    """ 소스에서 처리할 이벤트 가져오기 """

  def identify_events(self):
    """ 가져온 데이터를 파싱하여 도메인 객체 이벤트로 변환 """

  def stream_events(self):
    """ 파싱하 이벤트를 외부 에이전트로 전송 """
```

* 이 코드의 문제점
  * 특정 소스로 부터 로그를 가져오는 로더 기능
    * 데이터 소스에 연결한다.
    * 데이터를 로드한다.
    * 데이터를 필요하 모양으로 파싱하다.
  * 데이터 구조가 바뀌면 파싱하고 전송하는 부분을 모두 수정해야 한다.

### 책임 분산

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/1_srp_2.png" width="300"/>
</div>

* 메서드 한 개당 하나의 클래스로 분리하여 각 클래스마다 단일 책임을 갖게 한다.
  * 각 클래스마다 명확한 기능을 갖게 되다.
  * 기능별로 클래스로 캡슐화 된다.
  * 각 클래스의 유지보수가 쉽다.
  * 그렇다고 클래스 하나당 메서드가 반드시 한개여야 한다느 것은 아니다. 처리할 관심사가 같은 경우 하나의 클래스에 여러 메서드를 추가할 수 있다.

[목차로](./summary.md)