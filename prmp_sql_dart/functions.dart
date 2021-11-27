import 'bases.dart';

class Function extends Base {
  dynamic first, second;
  Function(this.first, {this.second});

  @override
  String toString() {
    String text = name;
    if (first != null) text += "($first}";
    if (second != null) text += ", $second";
    text += ")";
    return text;
  }
}

class One_Value extends Function {
  One_Value(first) : super(first);
}

class Two_Value extends Function {
  Two_Value(first, second) : super(first, second: second);
}

class AVG extends One_Value {
  AVG(first) : super(first);
}

class COUNT extends One_Value {
  COUNT(first) : super(first);
}

class MAX extends One_Value {
  MAX(first) : super(first);
}

class MIN extends One_Value {
  MIN(first) : super(first);
}

class SUM extends One_Value {
  SUM(first) : super(first);
}

class ROUND extends Two_Value {
  ROUND(column, integer) : super(column, integer);
}
