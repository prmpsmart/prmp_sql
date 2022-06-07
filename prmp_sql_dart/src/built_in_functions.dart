// ignore_for_file: camel_case_types, non_constant_identifier_names

import './bases.dart';

class Built_in_Function with Base {
  List<String> ARGS_MODIFIERS = [];
  int len = 0;
  int len_a = 0;
  List args = [];

  Built_in_Function(this.args) {
    len = args.length;
    len_a = ARGS_MODIFIERS.length;
  }

  @override
  String toString() {
    String _name = name;
    var l = len;
    var la = len_a;
    var args_m = ARGS_MODIFIERS;

    if (l > 0) {
      _name += '(';
      if (l == 1)
        _name += '${CONSTANT(args[0])}';
      else if ((l == 2) && (la == 2))
        _name += "${args[0]} ${args_m[0]} ${args[1]}";
      else if ((l == 2) && (la == 2))
        _name += "${args_m[0]} ${args[0]} ${args_m[1]} ${args[1]}";
      _name += ")";
    }

    return _name;
  }
}

// "The number of bits in a bit string"
class BIT_LENGTH extends Built_in_Function {
  BIT_LENGTH(String string) : super([CONSTANT(string)]);
}

// "The value, converted to the specified data type (e.g., a date converted to a character string)"
class CAST extends Built_in_Function {
  List<String> ARGS_MODIFIERS = ['AS'];

  CAST(value, data_type) : super([value, data_type]);
}

// "The length of a character string"
class CHAR_LENGTH extends BIT_LENGTH {
  CHAR_LENGTH(String string) : super(string);
}

// "A string converted as specified by a named conversion function"
class CONVERT extends Built_in_Function {
  List<String> ARGS_MODIFIERS = ['USING'];

  CONVERT(string, conv) : super([string, conv]);
}

// "The current date"
class CURRENT_DATE extends Built_in_Function {
  CURRENT_DATE(List args) : super(args);
}

// "The current time, with the specified precision"
class CURRENT_TIME extends Built_in_Function {
  CURRENT_TIME(precision) : super([precision]);
}

// "The current date and time, with the specified precision"
class CURRENT_TIMESTAMP extends Built_in_Function {
  CURRENT_TIMESTAMP(precision) : super(precision);
}

// "The specified part (DAY, HOUR, etc.) from a DATETIME value"
class EXTRACT extends Built_in_Function {
  List<String> ARGS_MODIFIERS = ['FROM'];

  EXTRACT(part, source) : super([part, source]);
}

// "A string converted to all lowercase letters"
class LOWER extends BIT_LENGTH {
  LOWER(String string) : super(string);
}

// "The number of 8-bit bytes in a character string"
class OCTET_LENGTH extends BIT_LENGTH {
  OCTET_LENGTH(String string) : super(string);
}

// "The position where the target string appears within the source string"
class POSITION extends Built_in_Function {
  List<String> ARGS_MODIFIERS = ['IN'];

  POSITION(target, source) : super([target, source]);
}

// "A portion of the source string, beginning at the nth character, for a length of len"
class SUBSTRING extends Built_in_Function {
  List<String> ARGS_MODIFIERS = ['FROM', 'FOR'];

  SUBSTRING(source, n, len) : super([source, n, len]);
}

// "A string translated as specified by a named translation function"
class TRANSLATE extends Built_in_Function {
  List<String> ARGS_MODIFIERS = ['USING'];

  TRANSLATE(string, trans) : super([CONSTANT(string), trans]);
}

// "A string with char trimmed off"
class TRIM extends Built_in_Function {
  List<String> ARGS_MODIFIERS = ['FROM'];
  String ADD_MODIFIERS = '';

  TRIM(char, string) : super([CONSTANT(char), CONSTANT(string)]) {
    if (ADD_MODIFIERS.isNotEmpty) ARGS_MODIFIERS.insert(0, ADD_MODIFIERS);
  }

  @override
  String get name {
    String nm = super.name;
    return nm.split("_")[0];
  }
}

// "A string with both leading and trailing occurrences of char trimmed off"
class TRIM_BOTH extends TRIM {
  String ADD_MODIFIERS = 'BOTH';

  TRIM_BOTH(char, string) : super(char, string);
}

// "A string with any leading occurrences of char trimmed off"
class TRIM_LEADING extends TRIM {
  String ADD_MODIFIERS = 'LEADING';

  TRIM_LEADING(char, string) : super(char, string);
}

// "A string with any trailing occurrences of char trimmed off"
class TRIM_TRAILING extends TRIM {
  String ADD_MODIFIERS = 'TRAILING';

  TRIM_TRAILING(char, string) : super(char, string);
}

// "A string converted to all uppercase letters"
class UPPER extends BIT_LENGTH {
  UPPER(String string) : super(string);
}
