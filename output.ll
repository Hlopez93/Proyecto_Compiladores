; ModuleID = "module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 10, i32* %"x"
  %".3" = load i32, i32* %"x"
  %".4" = bitcast [4 x i8]* @"fmt_int_2" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".3")
  %"y" = alloca i32
  store i32 20, i32* %"y"
  %".7" = load i32, i32* %"x"
  %".8" = load i32, i32* %"y"
  %".9" = add i32 %".7", %".8"
  %".10" = bitcast [4 x i8]* @"fmt_int_3" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %".9")
  ret i32 0
}

@"fmt_int_2" = constant [4 x i8] c"%d\0a\00"
@"fmt_int_3" = constant [4 x i8] c"%d\0a\00"