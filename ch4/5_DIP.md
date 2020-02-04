[위로](./README.md)

## 5. 의존성 역전 (DIP)

> 의존성 주입(Dependency Injection, DI)은 프로그래밍 에서 구성요소간의 의존 관계가 소스코드  내부가 아닌 외부의 설정파일 등을 통해 정의되게 하는 디자인 패턴   중의 하나이다. (출처: 위키백과)

* 질문 : 의존성을 역전시키려면 의존성을 주입해주는 프레임워크를 만들어야 한다. 파이썬은 주로 의존성 역전을 위해 어떤 프레임워크(혹은 컨테이너)를 사용하는가?
* Django 같은 웹 프레임워크에서 주로 사용한다.


### 이벤트 모니터링 시스템 설계하기

> EventStreamer 가 이벤트를 수집해서 Syslog 에 이벤트를 스트림으로 전송한다. EventStreamer 는 이벤트를 다수의 Syslog 클라이언트에게 전송한다.

#### 엄격한 의존의 예

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/5_dip_1.png" width="300"/>
</div>

* EventStreamer 는 Syslog 리스트를 가지고 있다.
* 이벤트가 수집되면 Syslog 들에게 각각 send() 한다.
* Syslog 로 데이터를 보내는 방식이 변경되면 EventStreamer 를 수정해야 한다.
* 목적지를 수정하거나 새로운 목적지가 추가된다면 stream() 메쏘드를 변경해야 한다.

#### 의존성을 거꾸로

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/5_dip_2.png" width="400"/>
</div>

* Syslog 를 인터페이스로 선언한다. (Python 에서는 구현하지 않은 pass 메쏘드를 만들어 둔다.)
* 이벤트를 가져갈 목적지마다 Syslog 구현체를 만든 다음 EventStreamer 에게 주입해 준다.
* EventStreamer 가 수정되거나 대상 클라이언트가 추가 되더라도 안전한 구조가 된다.

### **파이썬에서 구지 인터페이스를 선언할 필요가 있는가?**

* 파이썬은 덕 타이핑을 선호하기 때문에 구지 인터페이스를 선언하지 않더라도 send() 메쏘드만 있으면 되지 않은가? ---> 맞다. 구지 인터페이스를 선언하지 않고도 쓸 수 있다.
* 그러나 그렇다 하더라도 추상 기본 클래스(인터페이스)를 선언해서 사용하는 것이 좋은 습관이다. 덕 타이핑을 사용하면 모델의 가독성이 높아져서 이해하기 쉬워진다(???)
* **의문** : 저자는 추상 기본 클래스를 선언하고 확장하는 것이 덕 타이핑이라고 얘기하는데 .... 이건 덕 타이핑은 추상 기본 클래스를 선언하지 않더라도 처리해준다는 의미 아닌가?

[목차로](./README.md)