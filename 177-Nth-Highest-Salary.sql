CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) 
RETURNS TABLE (Salary INT) AS $$
BEGIN
  if N <= 0 then 
    return query select NULL :: INT;
 else 
  RETURN QUERY
    select distinct e.salary from Employee e order by e.salary desc offset N-1 limit 1;
end if;
END;
$$ LANGUAGE plpgsql;
