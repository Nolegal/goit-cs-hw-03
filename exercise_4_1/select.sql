-- 1. Отримати всі завдання певного користувача
Select *
FROM tasks
WHERE user_id = 1
-- 2. Вибрати завдання за певним статусом
SELECT tasks FROM status_id WHERE 'new'
-- 3. Оновити статус конкретного завдання
UPDATE status_id=1 WHERE 'in progress'
-- 4. Отримати список користувачів, які не мають жодного завдання
SELECT users WHERE NOT IN tasks
-- 5. Додати нове завдання для конкретного користувача
INSERT tasks FOR user_id=1
-- 6. Отримати всі завдання, які ще не завершено
GET*FROM tasks WHERE status_id 'new' AND 'in progress'
-- 7. Видалити конкретне завдання
DELETE tasks WHERE id=2
-- 8. Знайти користувачів з певною електронною поштою
SELECT usersWHERE email  LIKE '%@example.com'
-- 9. Оновити ім'я користувача
UPDATE users WHERE user_id=1
-- 10. Отримати кількість завдань для кожного статусу
SELECT COUNT (tasks), status_id GROUP BY status_id 
-- 11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
SELECT tasks LIKE JOIN '%@example.com'
-- 12. Отримати список завдань, що не мають опису
SELECT tasks WHERE NOT EXISTS
-- 13. Вибрати користувачів та їхні завдання, які є у статусі "в процесі"
SELECT users, tasks INNER JOIN WHERE status_id 'in progress'
-- 14. Отримати користувачів та кількість їхніх завдань
SELECT users COUNT (tasks) LEFT JOIN  GROUP BY tasks