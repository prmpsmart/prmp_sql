// ignore_for_file: camel_case_types

import './bases.dart';

class Function_ extends Base {
  dynamic first, second;
  Function_(this.first, {this.second});

  @override
  String toString() {
    String text = name;
    if (first != null) text += "($first";
    if (second != null) text += ", $second";
    text += ")";
    return text;
  }
}

class Function_One_Value extends Function_ {
  Function_One_Value(first) : super(first);
}

class Function_Two_Value extends Function_ {
  Function_Two_Value(first, second) : super(first, second: second);
}

class AVG extends Function_One_Value {
  AVG(first) : super(first);
}

class COUNT extends Function_One_Value {
  COUNT(first) : super(first);
}

class MAX extends Function_One_Value {
  MAX(first) : super(first);
}

class MIN extends Function_One_Value {
  MIN(first) : super(first);
}

class SUM extends Function_One_Value {
  SUM(first) : super(first);
}

class ROUND extends Function_Two_Value {
  ROUND(column, integer) : super(column, integer);
}
