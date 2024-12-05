-- skill_code보다 작고 가장 가까운 값부터 빼기
select distinct d.id, d.email, d.first_name, d.last_name
from developers d
join skillcodes s on (s.code & d.skill_code) > 0
where s.name in ('Python', 'C#')
order by d.id asc;