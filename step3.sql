use oldxian;
-- 3-2.查找计算机系每次考试学生的平均成绩(最终显示学生姓名, 考试名称, 平均分)。
SELECT 
    student.name, exam.exam_name,exam.garde
FROM
    student,
    exam
WHERE
    student.ID = exam.student_ID
        AND student.dept_mane = 'computer';

-- 3-3.查找女学霸（考试平均分达到80分或80分以上的女生的姓名, 分数）

 
 SELECT 
    student.name, exam.garde
FROM
    student,
    exam
WHERE
    student.ID = exam.student_ID
        AND student.sex = 'f'
        AND exam.garde >= 80;

-- 3-4.找出人数最少的院系以及其年度预算。
SELECT 
    student.dept_mane, department.budget
FROM
    student,
    department
WHERE
    student.dept_mane = department.dept_mane 
group by dept_mane 
having 
    SUM(dept_mane)=MIN(SUM(dept_mane = 'computer')
    AND SUM(dept_mane = 'biology')
    AND SUM(dept_mane = 'physics')
    AND SUM(dept_mane = 'new')
    AND SUM(dept_mane = 'math'));
    
-- 3-5.计算机系改名了，改成计算机科学系（comp. sci.）
update department , student set dept_mane= 'comp. sci.' where dept_mane= 'computer';

-- 3-6.修改每个系的年度预算，给该系的每个学生发2000元奖金。（修改每个系的年度预算为 原预算+该系人数*2000）。
update department set budget= budget*SUM(student.dept_mane = 'biology') where dept_mane= 'biology';
update department set budget= budget*SUM(student.dept_mane = 'computer') where dept_mane= 'computer';
update department set budget= budget*SUM(student.dept_mane = 'physics') where dept_mane= 'physics';
update department set budget= budget*SUM(student.dept_mane = 'new') where dept_mane= 'new';
update department set budget= budget*SUM(student.dept_mane = 'math') where dept_mane= 'math';

-- 3-7.向department表中插入一条数据, dept_name属性的值为avg_budget, building为空, 年度预算为所有院系的年度预算平均值.
insert into department values('avg_budget',NULL,avg(budget));

-- 3-8. 删除计算机系中考试成绩平均分低于70的学生.
delete from student where student.ID = exam.student_ID and exam.garde<70 and student.dept_mane='computer';

-- 3-9.找出所有正在谈恋爱,但是学习成绩不佳(考试平均分低于75)的学生,强制将其情感状态改为单身.
update student set emotion_state = 'single' where emotion_state = 'loving' and exam.garde<70;
