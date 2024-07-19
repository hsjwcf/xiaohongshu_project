from prompt_template import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
# 解析JSON数据为指定类型
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from xiaohongshu_model import Xiaohongshu

# import os


def generate_xiaohongshu(theme, openai_api_key):
    # 1. 定义模板
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])

    # 2. 定义大模型
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key,openai_api_base = "https://api.aigc369.com/v1")
    # 3. 实例化解析器对象并指定将返回的JSON字符串还原成Xiaohongshu类型
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    # 4. 定义链
    chain = prompt | model | output_parser
    # 5. 调用链的invoke()方法给模板中的变量赋值，并将模板传递给大模型，将大模型的输出给解析器,将大模型返回的JSON字符串转化成Xiaohongshu类型
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    # 返回Xiaohongshu类型
    return result


# result = generate_xiaohongshu("大模型", os.getenv("OPENAI_API_KEY"))
# print("result=",result)
# print("type=",type(result))
