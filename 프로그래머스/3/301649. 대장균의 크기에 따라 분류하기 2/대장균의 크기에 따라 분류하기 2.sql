select id, 
case
when s.ranks / cnts <= 0.25 then 'CRITICAL'
when s.ranks / cnts <= 0.5 then 'HIGH'
when s.ranks / cnts <= 0.75 then 'MEDIUM'
else 'LOW'
end as 'COlOnY_NAME'
from (select *,
      rank() over(order by size_of_colony desc) as ranks,
      count(*) over() as cnts from ecoli_data) as s
order by 1
    