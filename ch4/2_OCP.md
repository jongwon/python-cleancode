[위로](./summary.md)



## 2. 개방/패쇄 원칙 (OCP)

* **하나의 모듈은 개방되어 있으면서도 폐쇄되어야 한다.(? 뭔소린가)**
* 클래스(모듈)를 설계 할 때 클래스의 확장에는 개방되어 있어야 하고, 수정에는 폐쇄되어 있어야 한다는 원칙. ---> 그래야 유지보수가 쉽다.
* 새로운 요구 사항이 발생했을 때 새로운 것을 추가만 할 뿐 기존 코드는 그대로 유지해야 한다는 뜻...(무슨 뜬구름 잡는 소리인가)

> 질문 : 파이썬은 기본적으로 모든 데이터와 메서드가 public 인 것으로 알고 있다. close 를 한다면 어떤 방법으로 close 한다는 것인가? 문법만으로는 close 할 수 있는 방법이 없는 것 아닐까?

### 개방/패쇄 원칙을 따르지 않을 경우 유지보수의 어려움

* 잘 못된 코드의 예

``` python
class Event:
  def __init__(self, raw_data):
    self.raw_data = raw_data

class LoginEvent(Event):
  pass

class LogoutEvent(Event):
  pass

class SystemMonitor:
  def __init__(self, event_data):
    self.event_data = event_data

  def identify_event(self):
    if(self.event_data["before"]["session"] == 0 and self.event_data["after"]["session"] == 1):
      return LoginEvent(self.event_data)
    if(self.event_data["before"]["session"] == 1 and self.event_data["after"]["session"] == 0)
      return LogoutEvent(self.event_data)
    return UnknownEvent(self.event_data)
```

* 이 코드의 문제점 : 수정을 위해 닫히지 않았다.

### 확장성을 가진 이벤트 시스템으로 리펙토링

* 목적 : 새로운 이벤트가 추가되더라도 기존 소스가 수정되지 않게 하라!

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/2_ocp_1.png" width="300"/>
</div>

* 소스 코드 예제 : openclosed_2.py
* Event 에 meets_condition 이라는 staticmethod 를 두어 변경가능성을 닫았다.(?)

### 이벤트 시스템 확장

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/2_ocp_2.png" width="400"/>
</div>

* 소스 코드 예제 : openclosed_3.py
* 기존 코드를 전혀 수정하지 않고 TransactionEvent 타입을 새로 추가했다.

### OCP 최종 정리

* 코드를 변경하지 않고 기능을 확장하기 위해서는 보호하려는 추상화에 대해서 적절한 폐쇄를 해야 한다. 이 경우 meets_condition(event_data: dict) 라는 staticmethod 를 정의한 것이 폐쇄라고 볼 수 있다.

[목차로](./summary.md)