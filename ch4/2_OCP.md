[위로](./summary.md)



## 2. 개방/패쇄 원칙 (OCP)

* **하나의 모듈은 개방되어 있으면서도 폐쇄되어야 한다.(? 뭔소린가)**
* 클래스(모듈)를 설계 할 때 클래스의 확장에는 개방되어 있어야 하고, 수정에는 폐쇄되어 있어야 한다는 원칙. ---> 그래야 유지보수가 쉽다.
* 새로운 요구 사항이 발생했을 때 새로운 것을 추가만 할 뿐 기존 코드는 그대로 유지해야 한다는 뜻...(무슨 뜬구름 잡는 소리인가)

> 질문 : 파이썬은 기본적으로 모든 데이터와 메서드가 public 인 것으로 알고 있다. close 를 한다면 어떤 방법으로 close 한다는 것인가? 문법만으로는 close 할 수 있는 방법이 없는 것 아닐까?

### 개방/패쇄 원칙을 따르지 않을 경우 유지보수의 어려움

### 확장성을 가진 이벤트 시스템으로 리펙토링

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/2_ocp_1.png" width="300"/>
</div>

### 이벤트 시스템 확장

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/2_ocp_2.png" width="400"/>
</div>
### OCP 최종 정리

[목차로](./summary.md)