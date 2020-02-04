[위로](./README.md)


## 3. 리스코프 치환 원칙 (LSP)

> 만약 S가 T의 하위 타입이라면 프로그램을 변경하지 않고 T 타입의 객체를 S 타입의 객체로 치환 가능해야 한다.

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/3_lsp_1.png" width="400"/>
</div>
* 하위 클래스는 상위 클래스에서 정의한 계약을 그대로 따르도록(위배되지 않도록) 디자인 해야 한다.

### 도구를 사용해 LSP 문제 검사하기

Mypy 나 Pylint 같은 도구를 이용해 검사한다.(1장에서 설명)

``` python
class Event:
    def meets_condition(self, event_data:dict) -> bool:
        return False

class LoginEvent(Event):
    def meets_condition(self, event_data:list) -> bool:
        return bool(event_data)

lsp_1.py:9: error: Argument 1 of "meets_condition" is incompatible with supertype "Event"; supertype defines the argument type as "Dict[Any, Any]"
Found 1 error in 1 file (checked 1 source file)

```

* 이 코드는 Mypy 검사를 하면 타입 에러가 난다.

#### 메서드 서명의 잘못된 데이터타입 검사

* 코드 전체에 어노테이션을 기술하고 Mypy를 설정했다면 기본 타입 오류와 LSP 위반 여부를 바로 확인할 수 있다.
* 코드 예제

``` python
class Event:
    def meets_condition(self, event_data:dict) -> bool:
        return False

class LoginEvent(Event):
    def meets_condition(self, event_data:list) -> bool:
        return bool(event_data)

lsp_1.py:9: error: Argument 1 of "meets_condition" is incompatible with supertype "Event"; supertype defines the argument type as "Dict[Any, Any]"
Found 1 error in 1 file (checked 1 source file)

```

#### Pylint로 호환되지 않는 서명 검사

* 메서드의 파라미터 타입이 다른 것이 아니라 메서드의 인자 개수가 다르거나 형태가 다른 경우 오류를 감지하기 어렵다.
* Mypy 나 Pylint 로 이런 오류를 잡을 수 있다(???)고 한다.

``` python
class Event:
    def meets_condition(self, event_data:dict) -> bool:
        return False

class LoginEvent(Event):
    def meets_condition(self, event_data:dict, override: bool) -> bool:
        return bool(event_data)

lsp_2.py:9: error: Signature of "meets_condition" incompatible with supertype "Event"
Found 1 error in 1 file (checked 1 source file)
```

### 애매한 LSP 위반 사례

* 하위 클래스는 부모 클래스에 정의된 것보다 사전조건을 엄격하게 만들면 안 된다.
* 하위 클래스는 부모 클래스에 정의된 것보다 약한 사후조건을 만들면 안 된다.

<div style="text-align:center;">
<img src="https://github.com/jongwon/python-cleancode/raw/master/ch4/images/3_lsp_2.png" width="300"/>
</div>


``` python
class Event:
  
```

### LSP 최종 정리


[목차로](./README.md)