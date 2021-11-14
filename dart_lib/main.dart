import 'bases.dart';
import 'keywords.dart';

void main(List<String> args) {
  print(
    VALUES(['loce', 'jummy', 'grace', 'loveth']),
  );
  print(
    MULTI_VALUES(
      [
        VALUES(['loce', 'jummy', 'grace', 'loveth']),
        VALUES(['loce', 'jummy', 'grace', 'loveth']),
        VALUES(['loce', 'jummy', 'grace', 'loveth']),
      ],
    ),
  );
  String name = 'AS';
  bool y = Reserved_Keywords.values.contains(name);
  print(Reserved_Keywords.ABS);
}
