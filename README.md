Проект представляет из себя backend для интернет-магазина


Запуск: 

```docker-compose up --build -d```

Архитектура проекта:

![image](https://github.com/user-attachments/assets/8bdafb82-8517-4155-9af9-4519900ae654)



1 пользователь

![2_1](https://github.com/pligy/store/assets/62108982/3635418b-8e34-45d5-8333-bc5f13cf3b08)
![3](https://github.com/pligy/store/assets/62108982/abbb6f12-30cf-40f2-98f3-fdbc2aee7733)
![4](https://github.com/pligy/store/assets/62108982/6bcecbfd-4cc6-4465-a0ee-c903f2a015c5)

Нагрузочное тестирование:

10/1 3/1 18/1 10/10 (users/ramp up)

nginx load balancer + 2 nginx + 2 be + 2 pgpool + 2 pg

![image](https://github.com/pligy/store/assets/62108982/66dfe88c-115d-40ae-8604-9b0d4442a801)
![image](https://github.com/pligy/store/assets/62108982/470f4e1e-7385-413d-8ec7-bc463fd3305f)
![image](https://github.com/pligy/store/assets/62108982/509e13df-8041-43eb-be07-015708f10fa2)


1 be + 1 pgpool + 2 pg

![image](https://github.com/pligy/store/assets/62108982/6d8bbd53-9164-40f6-be4c-9c1d238fb944)
![image](https://github.com/pligy/store/assets/62108982/8ac99a05-51f5-4540-b107-19c925602da1)
![image](https://github.com/pligy/store/assets/62108982/a65e34ef-b583-4077-9a44-6039e29bf1ca)


1 nginx + 2 be + 2 pgpool + 2 pg

![image](https://github.com/pligy/store/assets/62108982/4101bb9e-6abb-4b1e-8a4e-d733c28fb830)
![image](https://github.com/pligy/store/assets/62108982/3b4fbb5c-589e-4240-adcc-2a20825ee679)
![image](https://github.com/pligy/store/assets/62108982/bb0439c8-d09e-4222-a13e-31d61f0b7836)


nginx load balancer + 2 nginx + 2 be + 2 pgpool + 2 pg + 2 redis

![image](https://github.com/pligy/store/assets/62108982/3bef66e7-5faa-4ae5-b8bd-a53a429f3ffe)
![image](https://github.com/pligy/store/assets/62108982/2cdc036b-8778-44e5-9515-11b3362c2d66)
![image](https://github.com/pligy/store/assets/62108982/16cab931-35b1-4827-ad3e-41a6df048ffd)


1 be + 1 pgpool + 2 pg + 1 redis

![image](https://github.com/pligy/store/assets/62108982/15747342-c129-43ae-8c5e-899bde92caea)
![image](https://github.com/pligy/store/assets/62108982/e2397ac4-662d-4566-81f1-6f76dab94e39)
![image](https://github.com/pligy/store/assets/62108982/a9c5e414-dba8-4984-a649-05c6f8c85e87)

1 nginx + 2 be + 2 pgpool + 2 pg + 2 redis

![image](https://github.com/pligy/store/assets/62108982/4ae5ae3d-345f-4dda-918e-8f0d3ce19f04)
![image](https://github.com/pligy/store/assets/62108982/2891ced8-57c1-4036-89ef-211822b7c36f)
![image](https://github.com/pligy/store/assets/62108982/409c7c0e-876d-4c21-b197-69e51fb0f279)




