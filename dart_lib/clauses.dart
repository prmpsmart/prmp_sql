import 'dart:indexed_db';

import 'operators.dart';
import 'bases.dart';

class Clause extends Name_Space_Base {
  dynamic? expression;

  Clause({this.expression});
  @override
  String toString() {
    String name = this.name;
    if (expression != null) name += " $expression";
    return name;
  }
}

class FROM extends Clause {}

class WHERE extends Clause {}

class GROUP_BY extends Clause {}

class HAVING extends Clause {}

class ORDER_BY extends Clause {
  ORDER_BY(columns) : super(expression: columns) {
    if (!(columns is Columns)) expression = Columns(columns);
  }
}

class SET extends Clause {
  // :values: tuple, list of length 2, or instance of EQUAL
  SET(List values) : super() {
    int l = values.length;
    if (l > 0) {
      List<Type> ll = [];
      values.forEach((element) {
        ll.add(element.runtimeType);
      });
      if (ll.contains(Columns)) {
        // "Only one Columns object should be parsed."
        assert(l == 1);
        expression = values[0];
      } else {
        List columns = [];
        values.forEach((value) {
          dynamic equal = null;
          if (value is List) {
            // "Tuple or List must be of len 2, (column_name1, value1) i.e column_name1 = value1"
            assert(value.length == 2);
            equal = EQUAL(value[0], value[1]);
          } else if ((value is EQUAL) || (value is SET)) equal = value;

          equal.parenthesis = false;
          columns.add(equal);
        });
        expression = Columns(columns);
      }
    }
  }
}

class INDEX extends Clause {
  INDEX(expression) : super(expression: expression);

  @override
  String toString() => "$name $expression";
}

class UNIQUE_INDEX extends INDEX {
  UNIQUE_INDEX(expression) : super(expression);
}
