class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "")
            return f"[fallback resolved] {name}"
        raise AttributeError(f"{self.__class__.__name__}에는 {attr} 속성이 없음.")  # 이 에러가 발생하면 기본 값을 반환한다.


dyn = DynamicAttributes("value")
print(dyn.attribute)
print(dyn.fallback_test)
dyn.__dict__["fallback_new"] = "new value"  # __getattr__ 메소드가 호출되지 않는다.
print(dyn.fallback_new)
print(getattr(dyn, "something", "default"))  # __getattr__ 메소드가 호출되지 않는다. 그래서 에러가 안난다.
