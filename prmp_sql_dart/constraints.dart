import 'bases.dart';

class Constraint extends Base {
  dynamic value;
  Constraint(this.value);

  @override
  String get name => super.name.replaceAll("_", " ");

  @override
  String toString() => "$value $name";
}

class NOT_NULL extends Constraint {
  NOT_NULL(value) : super(value);
}

class PRIMARY_KEY extends Constraint {
  PRIMARY_KEY(value) : super(value);
}

class UNIQUE extends Constraint {
  UNIQUE(value) : super(value);
}

class FOREIGN_KEY extends Constraint {
  FOREIGN_KEY(value) : super(value);
}

class CHECK extends Constraint {
  CHECK(value) : super(value);
}

class DEFERRABLE extends Constraint {
  DEFERRABLE(value) : super(value);
}

class NOT_DEFERRABLE extends Constraint {
  NOT_DEFERRABLE(value) : super(value);
}

class INITIALLY_IMMEDIATE extends Constraint {
  INITIALLY_IMMEDIATE(value) : super(value);
}

class INITIALLY_DEFERRED extends Constraint {
  INITIALLY_DEFERRED(value) : super(value);
}
