; ModuleID = "module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"nums" = alloca i32*
  %".2" = alloca [5 x i32]
  %".3" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 0
  store i32 1, i32* %".3"
  %".5" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 1
  store i32 3, i32* %".5"
  %".7" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 2
  store i32 5, i32* %".7"
  %".9" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 3
  store i32 7, i32* %".9"
  %".11" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 4
  store i32 9, i32* %".11"
  %".13" = bitcast [5 x i32]* %".2" to i32*
  store i32* %".13", i32** %"nums"
  %"total" = alloca i32
  store i32 0, i32* %"total"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %"while_cond"
while_cond:
  %".18" = load i32, i32* %"i"
  %".19" = icmp slt i32 %".18", 5
  br i1 %".19", label %"while_body", label %"while_end"
while_body:
  %"r" = alloca i32
  %".21" = load i32*, i32** %"nums"
  %".22" = load i32, i32* %"i"
  %".23" = getelementptr i32, i32* %".21", i32 %".22"
  %".24" = load i32, i32* %".23"
  %".25" = srem i32 %".24", 2
  store i32 %".25", i32* %"r"
  %".27" = load i32, i32* %"r"
  %".28" = icmp eq i32 %".27", 0
  br i1 %".28", label %"then", label %"ifend"
while_end:
  %".42" = bitcast [17 x i8]* @"str_3" to i8*
  %".43" = bitcast [4 x i8]* @"str_4" to i8*
  %".44" = call i32 (i8*, ...) @"printf"(i8* %".43", i8* %".42")
  %".45" = call i32 @"fibonacci"(i32 20)
  %".46" = bitcast [4 x i8]* @"str_5" to i8*
  %".47" = call i32 (i8*, ...) @"printf"(i8* %".46", i32 %".45")
  %".48" = bitcast [14 x i8]* @"str_6" to i8*
  %".49" = bitcast [4 x i8]* @"str_7" to i8*
  %".50" = call i32 (i8*, ...) @"printf"(i8* %".49", i8* %".48")
  %".51" = load i32, i32* %"total"
  %".52" = bitcast [4 x i8]* @"str_8" to i8*
  %".53" = call i32 (i8*, ...) @"printf"(i8* %".52", i32 %".51")
  ret i32 0
then:
  %".30" = load i32, i32* %"total"
  %".31" = load i32*, i32** %"nums"
  %".32" = load i32, i32* %"i"
  %".33" = getelementptr i32, i32* %".31", i32 %".32"
  %".34" = load i32, i32* %".33"
  %".35" = add i32 %".30", %".34"
  store i32 %".35", i32* %"total"
  br label %"ifend"
ifend:
  %".38" = load i32, i32* %"i"
  %".39" = add i32 %".38", 1
  store i32 %".39", i32* %"i"
  br label %"while_cond"
}

define i32 @"fibonacci"(i32 %"n")
{
entry:
  %".3" = alloca i32
  store i32 %"n", i32* %".3"
  %".5" = load i32, i32* %".3"
  %".6" = icmp sle i32 %".5", 1
  br i1 %".6", label %"then", label %"ifend"
then:
  %".8" = load i32, i32* %".3"
  ret i32 %".8"
ifend:
  %".10" = load i32, i32* %".3"
  %".11" = sub i32 %".10", 1
  %".12" = call i32 @"fibonacci"(i32 %".11")
  %".13" = load i32, i32* %".3"
  %".14" = sub i32 %".13", 2
  %".15" = call i32 @"fibonacci"(i32 %".14")
  %".16" = add i32 %".12", %".15"
  ret i32 %".16"
}

@"str_3" = constant [17 x i8] c"Fibonacci(20) = \00"
@"str_4" = constant [4 x i8] c"%s\0a\00"
@"str_5" = constant [4 x i8] c"%d\0a\00"
@"str_6" = constant [14 x i8] c"Total pares: \00"
@"str_7" = constant [4 x i8] c"%s\0a\00"
@"str_8" = constant [4 x i8] c"%d\0a\00"