CREATE TABLE IF NOT EXISTS todo (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            item VARCHAR(255) NOT NULL
        )

INSERT INTO todo (item)
VALUES ('Learn SQL'), ('build a rest api'), ('write unit tests');

SELECT id, item from todo
where id = 'f8ce5a41-faa7-48c3-9649-a14f826fa3aa';

select id,item from todo;

Update todo
set item = 'Learn advanced SQL'
where id = 'f8ce5a41-faa7-48c3-9649-a14f826fa3aa';

delete from todo
where id ='bac9d176-33e2-430f-adf8-3aa8a6f17bda';