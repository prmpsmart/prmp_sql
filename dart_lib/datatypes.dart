import 'bases.dart';

class Data_Type extends Name_Space_Base {
  List ABBRS = [];
  String DESCRIPTION = "";
  List MODIFIERS = [];

  // "Data_Type only accept string type as column name"
  String column;
  dynamic first, second;

  Data_Type(this.column, {this.first, this.second}) {
    if (second != null)
      // "first must be provided to use second"
      assert(first != null);
    [first, second].forEach((element) {
      assert((element is int) || (element is double));
    });
  }
  @override
  String toString() {
    String text = "$column $name";
    if (first != null) {
      text += "($first";
      if (second! + null) text += ", $second";
      text += ")";
    }
    return text;
  }
}

class Just_Name extends Data_Type {
  Just_Name(name) : super(name);
}

class One_Value extends Data_Type {
  One_Value(name, first) : super(name, first: first);
}

class Two_Value extends Data_Type {
  Two_Value(name, first, second) : super(name, first: first, second: second);
}

class TEXT extends Just_Name {
  TEXT(name) : super(name);
}

class CHARACTER extends One_Value {
  List ABBRS = ["CHAR"];
  String DESCRIPTION = "Fixed-length character strings";

  CHARACTER(name, {first = 255}) : super(name, first);
}

class CHAR extends CHARACTER {
  CHAR(name) : super(name);
}

class CHARACTER_VARYING extends One_Value {
  List ABBRS = ["CHAR VARYING", "VARCHAR"];
  String DESCRIPTION = "Variable-length character strings";

  CHARACTER_VARYING(name, {first = 255}) : super(name, first);
}

class VARCHAR extends CHARACTER_VARYING {
  VARCHAR(name) : super(name);
}

class CHARACTER_LARGE_OBJECT extends One_Value {
  List ABBRS = ["CLOB"];
  String DESCRIPTION = "Large fixed-length character strings";

  CHARACTER_LARGE_OBJECT(name, first) : super(name, first);
}

class CLOB extends CHARACTER_LARGE_OBJECT {
  CLOB(name, first) : super(name, first);
}

class NATIONAL_CHARACTER extends One_Value {
  List ABBRS = ["NATIONAL CHAR", "NCHAR"];
  String DESCRIPTION = "Fixed-length national character strings";

  NATIONAL_CHARACTER(name, first) : super(name, first);
}

class NATIONAL_CHARACTER_VARYING extends One_Value {
  List ABBRS = ["NATIONAL CHAR VARYING", "NCHAR"];
  String DESCRIPTION = "Variable-length national character strings";

  NATIONAL_CHARACTER_VARYING(name, first) : super(name, first);
}

class NATIONAL_CHARACTER_LARGE_OBJECT extends One_Value {
  List ABBRS = ["NCLOB"];
  String DESCRIPTION = "Large variable-length national character strings";

  NATIONAL_CHARACTER_LARGE_OBJECT(name, first) : super(name, first);
}

class BIT extends One_Value {
  String DESCRIPTION = "Fixed-length bit strings";

  BIT(name, first) : super(name, first);
}

class BIT_VARYING extends One_Value {
  String DESCRIPTION = "Variable-length bit strings";

  BIT_VARYING(name, first) : super(name, first);
}

class BLOB extends Just_Name {
  BLOB(name) : super(name);
}

class BOOLEAN extends Just_Name {
  BOOLEAN(name) : super(name);
}

class INTEGER extends Just_Name {
  List ABBRS = ["INT"];
  String DESCRIPTION = "Integers";

  INTEGER(name) : super(name);
}

class INT extends INTEGER {
  INT(name) : super(name);
}

class SMALLINT extends Just_Name {
  String DESCRIPTION = "Small integers";

  SMALLINT(name) : super(name);
}

class NUMERIC extends Two_Value {
  List FUNCTIONAL_ARGS = [double, int];
  String DESCRIPTION = "Decimal numbers";

  NUMERIC(name, first, second) : super(name, first, second);
}

class DECIMAL extends Two_Value {
  List ABBRS = ["DEC"];
  List FUNCTIONAL_ARGS = [double, int];
  String DESCRIPTION = "Decimal numbers";

  DECIMAL(name, first, second) : super(name, first, second);
}

class FLOAT extends One_Value {
  List FUNCTIONAL_ARGS = [double];
  String DESCRIPTION = "Floating point numbers";

  FLOAT(name, first) : super(name, first);
}

class REAL extends Just_Name {
  String DESCRIPTION = "Low-precision doubleing point numbers";

  REAL(name) : super(name);
}

class DOUBLE_PRECISION extends Just_Name {
  String DESCRIPTION = "High-precision doubleing point numbers";

  DOUBLE_PRECISION(name) : super(name);
}

class DATE extends Just_Name {
  String DESCRIPTION = "Calendar dates";

  DATE(name) : super(name);
}

class TIME extends One_Value {
  List FUNCTIONAL_ARGS = [double];
  String DESCRIPTION = "Clock times";

  TIME(name, first) : super(name, first);
}

class TIME_WITH_TIME_ZONE extends One_Value {
  List FUNCTIONAL_ARGS = [double];
  String DESCRIPTION = "Clock times with time zones";

  TIME_WITH_TIME_ZONE(name, first) : super(name, first);
}

class TIMESTAMP extends One_Value {
  List FUNCTIONAL_ARGS = [double];
  String DESCRIPTION = "Dates and times";

  TIMESTAMP(name, first) : super(name, first);
}

class TIMESTAMP_WITH_TIME_ZONE extends One_Value {
  List FUNCTIONAL_ARGS = [double];
  String DESCRIPTION = "Dates and times with time zones";

  TIMESTAMP_WITH_TIME_ZONE(name, first) : super(name, first);
}

class INTERVAL extends Data_Type {
  String DESCRIPTION = "Time intervals";

  INTERVAL(String column) : super(column);
}

class XML extends Data_Type {
  //  (type modifier [secondary type modifier])
  String DESCRIPTION =
      "Character data formatted as Extensible Markup Language (XML)";

  XML(String column) : super(column);
}
