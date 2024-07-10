select em.name as "Employee" from Employee em
where
(em.managerId is not null) and 
(em.salary > (select mg.salary from Employee mg where mg.id = em.managerId))
