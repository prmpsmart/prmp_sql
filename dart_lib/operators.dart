import 'bases.dart';

class Operator with Base {
  bool parenthesis = true;
  bool LTR = true;
  // Operator value can not be [None, 0]
  String operator = '';
  // First value can not be [None, Empty string, 0]
  dynamic first, second;

  Operator(this.first, {this.second}) {
    assert(operator.isNotEmpty);

    if (second.runtimeType.toString() == 'SELECT') second.parenthesis = true;
  }
  @override
  String toString() {
    int ln = 0;
    if (first != null) ln += 1;
    if (second != null) ln += 1;

    String text = "";

    if (ln == 1) {
      if (LTR)
        text = "$operator $first";
      else
        text = "$first $operator";
      ;
    } else if (ln == 2) text = "$first $operator $second";

    if (parenthesis) text = "($text)";

    return text;
  }
}

class Two_Values extends Operator {
  String operator = "";

  Two_Values(first, second) : super(first, second: second);
}

class MINUS extends Two_Values {
  String operator = "-";

  MINUS(first, second) : super(first, second);
}

class PLUS extends Two_Values {
  String operator = "+";

  PLUS(first, second) : super(first, second);
}

class MULTIPLY extends Two_Values {
  String operator = "*";

  MULTIPLY(first, second) : super(first, second);
}

class DIVIDE extends Two_Values {
  String operator = "/";

  DIVIDE(first, second) : super(first, second);
}

class MODULO extends Two_Values {
  String operator = "%";

  MODULO(first, second) : super(first, second);
}

class EQUAL extends Two_Values {
  String operator = "=";

  EQUAL(first, second) : super(first, second);
}

class NOT_EQUAL extends Two_Values {
  String operator = "<>";

  NOT_EQUAL(first, second) : super(first, second);
}

class GREATER_THAN extends Two_Values {
  String operator = ">";

  GREATER_THAN(first, second) : super(first, second);
}

class LESS_THAN extends Two_Values {
  String operator = "<";

  LESS_THAN(first, second) : super(first, second);
}

class NOT_GREATER_THAN extends Two_Values {
  String operator = "!>";

  NOT_GREATER_THAN(first, second) : super(first, second);
}

class NOT_LESS_THAN extends Two_Values {
  String operator = "!<";

  NOT_LESS_THAN(first, second) : super(first, second);
}

class GREATER_THAN_EQUAL extends Two_Values {
  String operator = ">=";

  GREATER_THAN_EQUAL(first, second) : super(first, second);
}

class LESS_THAN_EQUAL extends Two_Values {
  String operator = "<=";

  LESS_THAN_EQUAL(first, second) : super(first, second);
}

// ---------------------------------------------------

class Name_Operator extends Operator {
  Name_Operator(first, {second}) : super(first, second: second) {
    operator = name.replaceAll("_", " ");
  }
}

class TOP extends Name_Operator {
  TOP(first) : super(first);
}

class AS extends Name_Operator {
  AS(first, second, {bool hide = false}) : super(first, second: second) {
    if (hide) {
      operator = "";
      parenthesis = false;
    }
  }

  @override
  String toString() => super.toString().replaceAll("  ", " ");
}

class TO extends AS {
  TO(first, second) : super(first, second);
}

class BETWEEN extends Name_Operator {
  dynamic third;

  BETWEEN(first, second, this.third) : super(first, second: second) {
    // "second and third value must be of same data_type";
    assert((first.runtimeType == second.runtimeType) &&
        (second.runtimeType == third.runtimeType));
  }

  @override
  String toString() {
    String text = super.toString();
    return "$text AND $third";
  }
}

class ESCAPE extends Name_Operator {
  ESCAPE(String first) : super(first) {
    // "ESCAPE character must be a a char like [s, t, etc]"
    assert(first.length == 1);

    this.first = CONSTANT(first);
  }
}

class LIMIT extends Name_Operator {
  LIMIT(first) : super(first);
}

class LIKE extends Name_Operator {
  List<String> WILDCARDS = ["%", "_", "[*...]", "[^...]", "[!...]"];
  ESCAPE? escape;

  LIKE(first, String second, {escape = null}) : super(first, second: second) {
    // "second value must be a string containing wildcards"

    if (escape is String) escape = ESCAPE(escape);
    this.escape = escape;
  }

  @override
  String toString() {
    String text = super.toString();
    if (escape != null) text = "$text $escape";
    return text;
  }
}

class IN extends Name_Operator {
  IN(first, second) : super(first, second: second) {
    assert((second.runtimeType.toString() == 'SELECT') || (second is Tuple));
  }
}

class EXISTS extends IN {
  EXISTS(first, second) : super(first, second);
}

class AND extends Name_Operator {
  AND(first, second) : super(first, second: second);
}

class NOT extends Name_Operator {
  bool parenthesis = false;

  NOT(first) : super(first);
}

class INTO extends NOT {
  INTO(first) : super(first);
}

class OR extends Name_Operator {
  OR(first, second) : super(first, second: second);
}

class DISTINCT extends Name_Operator {
  DISTINCT(first) : super(first) {
    assert((first is String) || (first is Columns));
  }
}

class COLLATE extends Name_Operator {
  bool parenthesis = false;

  COLLATE(first, second) : super(first, second: second);
}

class Name_Operator_F extends Name_Operator {
  bool LTR = false;
  bool parenthesis = false;

  Name_Operator_F(first, {second}) : super(first, second: second);
}

class IS_NULL extends Name_Operator_F {
  IS_NULL(first) : super(first);
}

class IS_NOT_NULL extends Name_Operator_F {
  IS_NOT_NULL(first) : super(first);
}

class ASC extends Name_Operator_F {
  ASC(first) : super(first);
}

class DESC extends Name_Operator_F {
  DESC(first) : super(first);
}

class ON extends Name_Operator_F {
  dynamic third;
  ON(first, second, third) : super(first, second: second) {
    assert((third is Tuple) || (third is Columns));

    if (third is Columns) third.parenthesis = true;
    this.third = third;
  }

  @override
  String toString() {
    var text = super.toString();
    return "$text $third";
  }
}

class _SET extends Name_Operator {
  bool parenthesis = false;

  _SET(first, second) : super(first, second: second);
}

class UNION extends _SET {
  UNION(first, second) : super(first, second) {
    if ((first is UNION) && !(second is UNION)) {
      dynamic middle = first;
      first = second;
      second = middle;
    }

    [first, second].forEach((element) {
      if (element is UNION) element.parenthesis = true;
    });
  }
}

class UNION_ALL extends UNION {
  UNION_ALL(first, second) : super(first, second);
}

class INTERSET extends _SET {
  INTERSET(first, second) : super(first, second);
}

// "Also called MINUS"
class EXCEPT extends _SET {
  EXCEPT(first, second) : super(first, second);
}

class JOIN extends _SET {
  JOIN(first, second) : super(first, second);

  String get string => super.toString();

  @override
  String toString() {
    return '$string;';
  }

  Statement_ operator +(other) =>
      Statement_('${this.toString()}  ${other.toString()}');
}

class INNER_JOIN extends JOIN {
  INNER_JOIN(first, second) : super(first, second);
}

class LEFT_JOIN extends JOIN {
  LEFT_JOIN(first, second) : super(first, second);
}

class RIGHT_JOIN extends JOIN {
  RIGHT_JOIN(first, second) : super(first, second);
}

class FULL_JOIN extends JOIN {
  FULL_JOIN(first, second) : super(first, second);
}

class FULL_OUTER_JOIN extends FULL_JOIN {
  FULL_OUTER_JOIN(first, second) : super(first, second);
}

class CROSS_JOIN extends JOIN {
  CROSS_JOIN(first, second) : super(first, second);
}

class NATURAL_JOIN extends JOIN {
  NATURAL_JOIN(first, second) : super(first, second);
}
