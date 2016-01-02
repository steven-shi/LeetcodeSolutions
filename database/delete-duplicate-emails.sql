#Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its #smallest Id.
#
#+----+------------------+
#| Id | Email            |
#+----+------------------+
#| 1  | john@example.com |
#| 2  | bob@example.com  |
#| 3  | john@example.com |
#+----+------------------+
#Id is the primary key column for this table.
#
#For example, after running your query, the above Person table should have the following rows:
#
#+----+------------------+
#| Id | Email            |
#+----+------------------+
#| 1  | john@example.com |
#| 2  | bob@example.com  |
#+----+------------------+


# Write your MySQL query statement below
delete from Person where id not in (
    select a.Id from (
    select min(Id) Id from Person
    group by Email) a
)
