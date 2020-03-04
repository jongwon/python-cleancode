## Doctest

- doctest 모듈은 독스트링 안에 대화형 파이썬 세션처럼 보이는 텍스트가 있는지를 검색한 후
- 해당 세션들을 실행하여 테스트를 수행한다.
- Doctest 는 일반적으로 상세 테스트를 하지 않고 주된 사용법을 알려주는 문서로서의 기능을 한다.
- Doctest 는 모듈을 실행할 때 자동으로 실행되도록 하는 것이 좋다.
  

``` python
def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

커맨드 라인에서 python module.py 를 쳐서 해당 모듈을 실행하면 doctest가 실행되고, 무언가 doctest에 기술한대로 동작하지 않는 경우에는 경고를 해준다.


## 참고
* [파이썬 코드 테스트](https://python-guide-kr.readthedocs.io/ko/latest/writing/tests.html)