# 开发者

安装antlr4, antlr4是一个语法解析器，能够支持很多的语法，目前支持的语言可以在这个库中找到
[https://github.com/antlr/grammars-v4/tree/master](https://github.com/antlr/grammars-v4/tree/master)

```sh
pip install antlr4-python3-runtime
```

```sh
antlr4 -Dlanguage=Python3 javaantlr/JavaLexer.g4 javaantlr/JavaParser.g4
antlr4 -Dlanguage=Python3 code2uml/antlr/cpp/CPP14Lexer.g4
antlr4 -Dlanguage=Python3 code2uml/antlr/cpp/CPP14Parser.g4
```

生成python的解析器

```sh
.
├── JavaLexer.g4
├── JavaLexer.interp
├── JavaLexer.py
├── JavaLexer.tokens
├── JavaParser.g4
├── JavaParser.interp
├── JavaParserListener.py
├── JavaParser.py
└── JavaParser.tokens
```

C++解析器存在问题:

1. 如果只使用这个lex和parser, 没有形成完整的语义树, 无法生成AST, 无法识别字段, 需要将python中的代码连接起来，需要从[https://github.com/antlr/grammars-v4/tree/master](https://github.com/antlr/grammars-v4/tree/master)中导入`CPP14ParserBase.py`和`transformGrammar.py`

transformGrammar.py是用于生成CPP14Parser.g4和CPP14Lexer.g4的工具，如果之前已经有现成的，可以不用执行
CPP14ParserBase.py只需要和生成后的文件集成在一起即可.

![alt text](img/develop/image.png)
