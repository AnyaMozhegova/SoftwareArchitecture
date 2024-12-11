# Диаграмма системного контекста

![image](https://github.com/user-attachments/assets/e34cbf38-71d6-4014-81bc-43ddfe08c6d9)

```PlantUML
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="Microservice\neight sided")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")

SHOW_PERSON_OUTLINE()

Person(user, Пользователь, "Настраивает параметры и получает персональное меню")
Person(admin, Администратор, "Управляет пользователями и системой")


Container(webFrontend, "Веб-интерфейс", "Web Application", "Генерация персонального меню на неделю")


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

![image](https://github.com/user-attachments/assets/abf3404c-dc97-4b29-81d5-df8b0eff17b5)

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
    Container(apiGateway, "API Gateway", "FastAPI", "Централизованный роутинг запросов")
    ContainerDb(mongoDB, "MongoDB", "NoSQL", "Хранение всех данных системы")
    Container(mlService, "ML-сервис", "FastAPI + PyTorch/Scikit-learn", "Рекомендует блюда и состав меню на основе предпочтений")
    ContainerDb(modelDB, "База данных модели", "NoSQL", "Хранение результатов обучения и данных модели")
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
# Диаграмма компонентов (Веб-приложение)
![image](https://github.com/user-attachments/assets/61c62e6f-5236-4083-a790-fc4677dcba7b)
```PlantUML
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="Microservice\neight sided")

SHOW_PERSON_OUTLINE()

Boundary(webFrontend, "Веб-интерфейс", "Container / React.js") {
    Component(ui, "UI", "Component: Frontend", "Представляет пользовательский интерфейс: ввод параметров, просмотр меню, настройка предпочтений")
    Component(httpClient, "HTTP Client", "Component: Network", "Обрабатывает запросы к API и получение данных")
    Component(router, "Router", "Component: Navigation", "Маршрутизация между страницами приложения")
    Component(stateManager, "State Manager", "Component: State Management", "Управляет состоянием приложения, включая данные пользователя и текущие настройки")
    Component(validation, "Validation Module", "Component: Logic", "Проверяет корректность введенных данных (например, бюджет, предпочтения, аллергии)")
}
System(ApiGateway, "ApiGateway", $type="Container / FastAPI") {
    
}

Person(user, Пользователь, "Взаимодействует с приложением через браузер")

Rel(user, ui, "Вводит параметры и просматривает меню")
Rel(ui, router, "Навигация между страницами")
Rel(ui, stateManager, "Обновление состояния интерфейса")
Rel(stateManager, validation, "Обновляет валидированные данные")
Rel(ui, httpClient, "Отправляет запросы к API")
Rel(stateManager, httpClient, "Передает текущие данные пользователя")
Rel(httpClient, "ApiGateway", "Отправляет запросы к API Gateway")

SHOW_LEGEND()
@enduml
```
# Диаграмма компонентов (Api-Gateway)
![image](https://github.com/user-attachments/assets/dce0d3e5-6f39-4c0e-a47d-5361f88c9291)

```PlantUML
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="Microservice\neight sided")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")

SHOW_PERSON_OUTLINE()
System(vb, "Веб-интерфейс", $type="Container / React.js") {
    
}
System(ml, "ML-servise", $type="Container / React.js") {
    
}
Boundary(apiGateway, "API Gateway", "Container / FastAPI") {
    Component(router, "Router", "Component: Routing", "Обрабатывает и направляет запросы в соответствующие сервисы")
    Component(authService, "Auth Service", "Component: Security", "Управляет аутентификацией пользователей")
    Component(dataAdapter, "Data Adapter", "Component: Data Layer", "Чтение и запись данных пользователей")
    Component(menuHandler, "Menu Handler", "Component: Logic", "Обрабатывает параметры и запрашивает рекомендации у ML-сервиса")
    Component(logger, "Logger", "Component: Monitoring", "Логирование запросов, ошибок и метрик")
}

ContainerDb(mongoDB, "MongoDB", "NoSQL", "Хранение данных пользователей: аллергии, предпочтений, истории меню")

Rel(vb, router, "Отправляет запросы на бэкенд")
Rel(menuHandler, ml, "Передает параметры для генерации меню")
Rel(router, authService, "Авторизация запросов")
Rel(router, dataAdapter, "Запросы к базе данных")
Rel(router, menuHandler, "Обработка параметров меню")
Rel(router, logger, "Логирование запросов")
Rel(dataAdapter, mongoDB, "Чтение и запись данных пользователей")
Rel(menuHandler, logger, "Логирование работы с параметрами меню")
Rel(menuHandler, router, "Возвращает результат обработки")

SHOW_LEGEND()
@enduml
```


