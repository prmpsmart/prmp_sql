import 'dart:indexed_db';

import 'operators.dart';
import 'bases.dart';

class Clause extends Name_Space_Base {
  dynamic expression;

  Clause(this.expression);
  @override
  String toString() {
    String name = this.name;
    if (expression != null) name += " $expression";
    return name;
  }
}

class FROM extends Clause {
  FROM(expression) : super(expression);
}

class WHERE extends Clause {
  WHERE(expression) : super(expression);
}

class GROUP_BY extends Clause {
  GROUP_BY(expression) : super(expression);
}

class HAVING extends Clause {
  HAVING(expression) : super(expression);
}

class ORDER_BY extends Clause {
  ORDER_BY(columns) : super(columns) {
    if (!(columns is Columns)) expression = Columns(columns);
  }
}

class SET extends Clause {
  // :values: tuple, list of length 2, or instance of EQUAL
  SET(List values) : super('') {
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
          } else if ([EQUAL,  SET].contains(value.runtimeType)) equal = value;

          equal.parenthesis = false;
          columns.add(equal);
        });
        expression = Columns(columns);
      }
    }
  }
}

class INDEX extends Clause {
  INDEX(expression) : super(expression);

  @override
  String toString() => "$name $expression";
}

class UNIQUE_INDEX extends INDEX {
  UNIQUE_INDEX(expression) : super(expression);
}
