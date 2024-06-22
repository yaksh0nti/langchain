from langchain_community.tools.custom_calculator import CustomCalculatorTool


def test_sum() -> None:
    tool = CustomCalculatorTool()
    result = tool.invoke({"a": 5, "b": 5})
    assert result == 25
