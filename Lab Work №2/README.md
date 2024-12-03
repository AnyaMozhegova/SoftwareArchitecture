# Диаграмма системного контекста
Было:
![лаб2(1)](https://github.com/user-attachments/assets/230f6df6-0a7e-4288-8ccd-2121d14b3ce7)

Стало:
![image](https://github.com/user-attachments/assets/42a39deb-3dcd-4bb9-8e45-a0d8deb07c22)
```PlantUML
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="Microservice\neight sided")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")

SHOW_PERSON_OUTLINE()

Person(user, Пользователь, "Настраивает параметры и получает персональное меню")
Person(admin, Администратор, "Управляет пользователями и системой")

Container_Boundary(menuApp, "Система составления меню") {
    Container(webFrontend, "Веб-интерфейс", "Web Application", "Генерация персонального меню на неделю")
}

Rel_D(user, webFrontend, "Использует для ввода данных и получения меню")
Rel_D(admin, webFrontend, "Управляет системой через интерфейс")
Rel_D(webFrontend, user, "Возвращает меню")

SHOW_LEGEND()
@enduml
```
# Диаграмма контейнеров с пояснениями по выбору базового архитектурного стиля / архитектуры уровня приложений

## Выбор архитектурного стиля: 
Выбор архитектурного стиля:

Выбранный стиль: Клиент-Серверная архитектура.
Обоснование:
* **Разделение функций:** Клиент-Серверная архитектура обеспечивает четкое разделение между клиентской частью (веб-интерфейс) и серверной частью (бэкенд), что упрощает управление сложной логикой формирования меню и рекомендаций.
* **Централизованное хранение данных:** Все данные о пользователях, меню, предпочтениях и ценах продуктов хранятся на сервере, что упрощает управление, резервное копирование и обеспечение безопасности.
* **Поддержка масштабирования:** Серверная часть может быть масштабирована для обработки большого числа запросов (например, за счет кластеризации FastAPI или использования контейнеризации).
* **Обеспечение совместимости:** Веб-интерфейс на React.js может работать как на настольных, так и на мобильных устройствах, обращаясь к серверу через HTTP/REST API.
* **Подготовка к реальным нагрузкам:** Сервер может эффективно обрабатывать пользовательские параметры и предоставлять персонализированные рекомендации в реальном времени.

## Модель взаимодействия компонентов:
* **Клиентская часть (React.js):**
Обеспечивает пользовательский интерфейс для настройки параметров и получения сгенерированного меню.
Работает через HTTP/REST API с серверной частью.
* **Бэкенд (FastAPI):**
Обрабатывает запросы от клиентов через API Gateway.
Координирует работу микросервисов, включая сервисы генерации меню, уведомлений и списков покупок.
* **ML-сервис:**
Использует машинное обучение для анализа предпочтений пользователя (аллергии, калорийность, бюджет, кухня).
Рекомендует блюда и меню на основе предоставленных данных.
* **Базы данных (MongoDB и Redis):**
MongoDB: Хранение информации о пользователях, рецептах, ценах продуктов и сгенерированных меню.
Redis: Кэширование уведомлений для обеспечения быстрой доставки.
* **Сторонние сервисы:**
Firebase/Push Notifications для отправки уведомлений пользователям.

Было:

![лаб2(2 1)](https://github.com/user-attachments/assets/c141a31d-136f-48e3-bd27-3d9bb54be688)
![лаб2(2 2)](https://github.com/user-attachments/assets/e0fd957e-8f10-4e85-a002-a576b6f8e6c9)

Стало:
![image](https://github.com/user-attachments/assets/1d3ebcdb-f121-4b99-97a1-a4d73bee5904)


```PlantUML
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="Microservice\neight sided")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")

SHOW_PERSON_OUTLINE()

Person(user, Пользователь, "Настраивает параметры и получает персональное меню")
Person(admin, Администратор, "Управляет системой и пользователями")

Container_Boundary(menuApp, "Система составления меню") {
    Container(webFrontend, "Веб-интерфейс", "React.js", "Предоставляет пользовательский интерфейс")
    
    Container_Boundary(backend, "Бэкенд") {
        Container(apiGateway, "API Gateway", "FastAPI", "Централизованный роутинг запросов")
    }
}

Container_Boundary(mongoDBContainer, "MongoDB") {
    Container(mongoDB, "MongoDB", "NoSQL", "Хранение всех данных системы")
}

Container_Boundary(mlServiceContainer, "ML-сервис") {
    Container(mlService, "ML-сервис", "FastAPI + PyTorch/Scikit-learn", "Рекомендует блюда и состав меню на основе предпочтений")
    Container(modelDB, "База данных модели", "NoSQL", "Хранение результатов обучения и данных модели")
}

Rel(user, webFrontend, "Взаимодействует через браузер или мобильное приложение")
Rel(admin, webFrontend, "Использует для управления системой")
Rel(webFrontend, apiGateway, "HTTP/REST", "Отправляет запросы в бэкенд")
Rel(apiGateway, mongoDB, "Сохраняет и читает данные пользователей")
Rel(mongoDB, apiGateway, "Возвращает результаты")
Rel(apiGateway, mlService, "Передаёт параметры для генерации меню")
Rel(mlService, apiGateway, "Возвращает рекомендации для меню")
Rel(mlService, modelDB, "Читает и сохраняет данные модели")

SHOW_LEGEND()
@enduml
```
