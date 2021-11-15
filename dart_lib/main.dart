import 'bases.dart';
import 'built_in_funtions.dart';
import 'keywords.dart';
import 'operators.dart';

void main(List<String> args) {
  // print(
  //   VALUES(['loce', 'jummy', 'grace', 'loveth']),
  // );
  // print(
  //   MULTI_VALUES(
  //     [
  //       VALUES(['loce', 'jummy', 'grace', 'loveth']),
  //       VALUES(['loce', 'jummy', 'grace', 'loveth']),
  //       VALUES(['loce', 'jummy', 'grace', 'loveth']),
  //     ],
  //   ),
  // );
  String name = 'AS';
  print(CURRENT_TIME(45));
  print(PLUS(45, 90));
  print(Tuple(['love', 'pink', 'hate', 'klitt', CONSTANT('value')]));
}
