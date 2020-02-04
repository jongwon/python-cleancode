[위로](./README.md)


## 4. 인터페이스 분리 원칙 (ISP)

* 작은 인터페이스를 선호
* 인터페이스란? 메서드 집합
* 덕 타이핑(duck typing) : 클래스를 구분지어주는 것은 궁극적으로 메서드의 형태이다.
* PEP-3119 : <https://www.python.org/dev/peps/pep-3119/>
  * 2007년 제안
  * ABC(Abstract Base Classes) 모듈을 도입함
  * isinstance() 와 issubclass() 메쏘드를 통해 특정 객체가 인터페이스를 구현하고 있는지를 체크할 수 있다.
* 질문 : 파이썬은 타입을 구분하지 않고 메서드가 있고/없고 만을 가지고 타입을 판단한다고 알고 있다. (duck typing) 그럼 파이썬에는 인터페이스를 따로 정의할 필요도 없고 인터페이스를 위한 별도의 문법이 필요 없는 것 아닌가?

### 너무 많은 일을 하는 인터페이스

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/4_isp_1.png" width="150"/>
</div>

### 인터페이스는 작을 수록 좋다

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/4_isp_2.png" width="350"/>
</div>

### 얼마나 작아야 할까

[목차로](./README.md)