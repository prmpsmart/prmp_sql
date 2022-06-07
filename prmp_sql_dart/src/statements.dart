// ignore_for_file: non_constant_identifier_names, camel_case_types, unused_shown_name

import './modifiers.dart';
import './constraints.dart';
import './datatypes.dart' show Data_Type, Data_Type_One_Value;
import './functions.dart' show Function_, Function_One_Value;
import './clauses.dart';
import './bases.dart';
import './operators.dart';

class SELECT extends Statement {
  String DESCRIPTION = "";
  bool parenthesis = false;

  dynamic columns;
  FROM? from;
  WHERE? where;
  GROUP_BY? group;
  HAVING? having;
  ORDER_BY? order;
  INTO? into;
  LIMIT? limit;
  int? offset;

  bool? distint;
  bool? all;

  SELECT(columns, from,
      {this.where,
      this.group,
      this.having,
      this.order,
      this.into,
      this.distint,
      this.all,
      this.limit,
      this.offset}) {
    bool allowed = false;
    if ((columns is String) || (columns is Columns) || (columns is Function_))
      allowed = true;

    if (allowed)
      this.columns = columns;
    else
      throw "type ($String, $Columns, $Function_) is expected not ${columns.runtimeType}.";
    if (from is String) from = FROM(from);
    this.from = from;
  }

  @override
  String toString() {
    String all_dis = ' ';
    if (all == true)
      all_dis = ' ALL ';
    else if (distint == true) all_dis = ' DISTINCT ';

    String default_ = "$name$all_dis$columns";
    if (into != null) default_ += " $into";

    default_ += " $from";
    if (where != null) default_ += " $where";
    if (group != null) default_ += " $group";
    if (having != null) default_ += " $having";
    if (order != null) default_ += " $order";
    if (parenthesis) default_ = "($default_)";
    return default_;
  }
}

class INSERT extends Statement {
  INTO? table;
  Columns? columns;
  dynamic values;
  WHERE? where;
  INSERT(table, {Columns? columns, values, where}) {
    if (columns != null) {
      assert(columns is Columns);
      columns.parenthesis = true;
    }

    assert([VALUES, MULTI_VALUES].contains(values.runtimeType));
    assert([String, Table].contains(table.runtimeType));

    this.table = INTO(table);
    this.columns = columns;
    this.values = values;
    this.where = where;
  }

  @override
  String toString() {
    String text = "$name $table";
    if (columns != null) text += " $columns";
    text += " $values";
    if (where != null) text += " $where";

    return text;
  }
}

class UPDATE extends Statement {
  dynamic table;
  SET set;
  WHERE? where;

  UPDATE(this.table, this.set, {this.where});

  @override
  String toString() {
    String text = "$name $table $set";
    if (where != null) text += " $where";
    return text;
  }
}

class DELETE extends Statement {
  dynamic table;
  WHERE? where;

  DELETE(this.table, {this.where});

  @override
  String toString() {
    String text = "$name FROM $table";
    if (where != null) text += " $where";
    return text;
  }
}

class One_Line extends Statement {
  dynamic expression;
  One_Line(this.expression);
  @override
  String toString() => '$name $expression';
}

class TRUNCATE_TABLE extends One_Line {
  TRUNCATE_TABLE(expression) : super(expression);
}

class New_Columns extends Columns {
  // :args: instances of (Data_Type, Constraint, Modifier)
  New_Columns(List args) : super([], parenthesis: true) {
    List columns = [];

    args.forEach((arg) {
      bool allowed = false;
      if (arg is Data_Type)
        allowed = true;
      else if (arg is Constraint)
        allowed = true;
      else if (arg is Modifier) allowed = true;

      if (allowed)
        columns.add(arg);
      else
        throw "args must be instances $allowed, not \"${arg.runtimeType}\"";
    });
    this.columns = columns;
  }
}

class CREATE extends One_Line {
  CREATE(expression) : super(expression);
}

class CREATE_TABLE extends CREATE {
  CREATE_TABLE(table, List new_columns_, {bool check_exist = false})
      : super('') {
    assert(new_columns_.isNotEmpty);
    New_Columns new_columns;

    if ((new_columns_.length == 1) && (new_columns_[0] is New_Columns))
      new_columns = new_columns_[0];
    else
      new_columns = New_Columns(new_columns_);

    assert(new_columns is New_Columns);
    String exist = check_exist ? 'IF NOT EXISTS' : '';
    expression = "$exist $table $new_columns";
  }
}

class CREATE_DATABASE extends CREATE {
  CREATE_DATABASE(expression) : super(expression);
}

class CREATE_VIEW extends CREATE {
  CREATE_VIEW(view, SELECT select) : super(AS(view, select));
}

class ADD_COLUMN extends One_Line {
  // :values: value in values can be a [str, Column, tuple, list, New_Column].
  // when value is a tuple or list, it must be of length 2, (column_name, datatype)
  ADD_COLUMN(List values) : super(null) {
    if (values.isNotEmpty) {
      int l = values.length;
      List<Type> ll = [];
      values.forEach((element) {
        ll.add(element.runtimeType);
      });
      if (ll.contains(Columns) || ll.contains(New_Columns)) {
        //  "Only one Columns object should be passed."
        assert(l == 1);
        expression = values[0];
      }
    }
    if (expression == null) {
      List columns = [];
      values.forEach((value) {
        dynamic col;
        if ([String, Column].contains(value.runtimeType))
          col = value;
        else
          throw "Value not supported.";

        columns.add(col);

        expression = New_Columns(columns);
      });

      if (expression == null) throw "Expression is not determined";
    }
  }
}

class ALTER_COLUMN extends ADD_COLUMN {
  ALTER_COLUMN(List values) : super(values);
}

class DROP_COLUMN extends One_Line {
  // :values: value in values can be a [str, Column, tuple, list, New_Column].
  // when value is a tuple or list, it must be of length 2, (column_name, datatype)
  DROP_COLUMN(List values) : super(null) {
    if (values.isNotEmpty) {
      int l = values.length;
      List<Type> ll = [];
      values.forEach((element) {
        ll.add(element.runtimeType);
      });
      if (ll.contains(Columns)) {
        //  "Only one Columns object should be passed."
        assert(l == 1);
        expression = values[0];
      }
    }
    if (expression == null) {
      List columns = [];
      values.forEach((value) {
        dynamic col;
        if ([String, Column].contains(value.runtimeType))
          col = value;
        else
          throw "Value not supported.";

        columns.add(col);

        expression = New_Columns(columns);
      });

      if (expression == null) throw "Expression is not determined";
    }
  }
}

class ALTER_TABLE extends One_Line {
  ALTER_TABLE(table, modifier) : super("$table $modifier");
}

class ALTER_DATABASE extends One_Line {
  ALTER_DATABASE(expression) : super(expression);
}

class DROP_DATABASE extends One_Line {
  DROP_DATABASE(expression) : super(expression);
}

class DROP_TABLE extends One_Line {
  DROP_TABLE(expression) : super(expression);
}

class DROP_VIEW extends One_Line {
  DROP_VIEW(expression) : super(expression);
}

class RENAME extends One_Line {
  RENAME(expression) : super(expression);
}

class RENAME_TABLE extends RENAME {
  RENAME_TABLE(TO expression) : super(expression);
}

class WITH extends Function_One_Value {
  WITH(first) : super(first);
}
