// ignore_for_file: non_constant_identifier_names, camel_case_types, unused_element

class Base {
  String DESCRIPTION = '';

  String get name => runtimeType.toString();

  void debug() => print(this);

  dynamic operator +(other) => '${this.toString()}  ${other.toString()}';
}

class CONSTANT extends Base {
  dynamic value;
  CONSTANT(value) {
    if ([int, double, bool].contains(value.runtimeType))
      this.value = value;
    else if (value is String)
      this.value = "'$value'";
    else
      throw ('value must be of type int, double, String not ${value.runtimeType}');
  }
  @override
  String toString() => value.toString();
}

class Tuple {
  List list = [];
  Tuple(this.list);

  @override
  String toString() {
    String text = list.join(', ');
    return '($text)';
  }
}

class Name_Space_Base extends Base {
  String get name => super.name.replaceAll('_', ' ');
}

class Statement extends Name_Space_Base {
  bool __bool__() {
    return true;
  }

  String get string => '';
  @override
  String toString() {
    return '$string;';
  }

  Statement_ operator +(other) =>
      Statement_('${this.toString()}  ${other.toString()}');
}

class Statement_ extends Statement {
  String _string;
  Statement_(this._string);

  @override
  String get string => _string;
}

class Table extends Base {
  String first;
  Table(this.first) {
    assert(first.isNotEmpty);
  }
  @override
  String toString() => first;
}

class Column extends Table {
  dynamic second;
  Column(first, {this.second = ''}) : super(first.toString());

  @override
  String toString() {
    String text = '$first';
    if (second.toString().isNotEmpty) text += '.$second';
    return text;
  }
}

class Columns extends Base {
  List<dynamic> columns;
  bool parenthesis;

  Columns(this.columns, {this.parenthesis = false});

  @override
  String toString() {
    String text = '';
    columns.forEach((column) {
      text += '$column, ';
    });

    text = text.substring(0, text.length - 2);
    if (parenthesis) text = '($text)';
    return text;
  }
}

class VALUES extends Columns {
  VALUES(List values, {insert: true}) : super([], parenthesis: true) {
    List _columns = [];
    if (insert) {
      values.forEach((element) {
        if (!(element is CONSTANT)) _columns.add(CONSTANT(element));
      });
      this.columns = _columns;
    }
  }
  String get string => super.toString();
  @override
  String toString() => '$name $string';
}

class MULTI_VALUES {
  List<VALUES> values;

  MULTI_VALUES(this.values) {
    values.forEach((element) {
      element.parenthesis = true;
    });
  }

  @override
  String toString() {
    String text = 'VALUES ';
    values.forEach((element) {
      text += '${element.string}, ';
    });
    text = text.substring(0, text.length - 2);
    return text;
  }
}
