# PRMP_SQL

> A convience SQL library.
>
>Still implementing the codes in *lib* and *lib2* to see the best implementations.

<br/>

## 1. Example 1

>    ``` SQL
>    -- SQL SELECT SYNTAX
>
>    SELECT NAME
>        FROM SALESREPS
>        WHERE (REP_OFFICE IN (22, 11, 12))
>        OR (MANAGER IS NULL AND HIRE_DATE >= '2006-06-01')
>        OR (SALES > QUOTA AND NOT SALES > 600000.0);
>    ```
>
>    ``` PY
>    # PYTHON SELECT SYNTAX
>    # formatted like this to show every parameters literally
>
>    SELECT(
>        Columns(
>            "NAME",
>        ),
>        FROM(
>            "SALESREPS",
>        ),
>        where=WHERE(
>            OR(
>                OR(
>                    IN(
>                        "REP_OFFICE",
>                        (22, 11, 12),
>                    ),
>                    AND(
>                        IS_NULL(
>                            "MANAGER",
>                        ),
>                        GREATER_THAN_EQUAL(
>                            "HIRE_DATE",
>                            CONSTANT(
>                                "2006-06-01",
>                            ),
>                        ),
>                    ),
>                ),
>                AND(
>                    GREATER_THAN(
>                        "SALES",
>                        "QUOTA",
>                    ),
>                    NOT(
>                        GREATER_THAN(
>                            "SALES",
>                            600000.00,
>                        ),
>                    ),
>                ),
>            )
>        ),
>    )
>    ```
>
>    ``` SQL
>    -- PYTHON OUTPUT
>
>    SELECT NAME
>        FROM SALESREPS
>    WHERE (((REP_OFFICE IN (22, 11, 12))
>        OR (MANAGER IS NULL AND (HIRE_DATE >= '2006-06-01')))
>        OR ((SALES > QUOTA) AND NOT (SALES > 600000.0)))
>    ```

<br/>

## 2. Example 2

>    ``` SQL
>    -- SQL SELECT SYNTAX
>
>    SELECT *
>    FROM city main_city
>    WHERE population > (
>    SELECT AVG(population)
>    FROM city average_city
>    WHERE average_city.country_id = main_city.country_id
>    );
>    ```
>
>    ``` PY
>    # PYTHON SELECT SYNTAX
>    # formatted like this to show every parameters literally
>
>    SELECT(
>        "*",
>        FROM(AS("city", "main_city", hide=True)),
>        where=WHERE(
>            GREATER_THAN(
>                "population",
>                SELECT(
>                    AVG("population"),
>                    FROM(AS("city", "average_city", hide=True)),
>                    where=WHERE(EQUAL(Column('country_id', table='average_city'), Column>('country_id', table='main_city'))),
>                ),
>            )
>        ),
>    )
>    ```
>
>    ``` SQL
>    -- PYTHON OUTPUT
>    SELECT * 
>    FROM city main_city
>    WHERE (population > (
>        SELECT AVG(population)
>        FROM city average_city
>        WHERE (average_city.country_id = main_city.country_id)))
>    ```
