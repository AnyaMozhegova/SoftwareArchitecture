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
![image](https://github.com/user-attachments/assets/b466416b-7e63-46ff-ad68-cd678cc5ec2d)



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
}


    ContainerDb(mongoDB, "MongoDB", "NoSQL", "Хранение всех данных системы")

    Container(mlService, "ML-сервис", "FastAPI + PyTorch/Scikit-learn", "Рекомендует блюда и состав меню на основе предпочтений")
    ContainerDb(modelDB, "База данных модели", "NoSQL", "Хранение результатов обучения и данных модели")


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
![image](https://github.com/user-attachments/assets/8703464d-a108-4042-9067-f4e1a210c5f3)

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

Person(user, Пользователь, "Взаимодействует с приложением через браузер")

Rel(user, ui, "Вводит параметры и просматривает меню")
Rel(ui, router, "Навигация между страницами")
Rel(ui, stateManager, "Обновление состояния интерфейса")
Rel(ui, validation, "Проверяет корректность данных")
Rel(validation, stateManager, "Обновляет валидированные данные")
Rel(ui, httpClient, "Отправляет запросы к API")
Rel(stateManager, httpClient, "Передает текущие данные пользователя")

SHOW_LEGEND()
@enduml

```
# Диаграмма компонентов (Api-Gateway)
![image](https://github.com/user-attachments/assets/4389af59-5816-4632-a992-ee81e5b482b1)
```PlantUML
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="Microservice\neight sided")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")

SHOW_PERSON_OUTLINE()

Boundary(apiGateway, "API Gateway", "Container / FastAPI") {
    Component(router, "Router", "Component: Routing", "Обрабатывает и направляет запросы в соответствующие сервисы")
    Component(authService, "Auth Service", "Component: Security", "Управляет аутентификацией пользователей")
    Component(dataAdapter, "Data Adapter", "Component: Data Layer", "Чтение и запись данных пользователей")
    Component(menuHandler, "Menu Handler", "Component: Logic", "Обрабатывает параметры и запрашивает рекомендации у ML-сервиса")
    Component(logger, "Logger", "Component: Monitoring", "Логирование запросов, ошибок и метрик")
}

ContainerDb(mongoDB, "MongoDB", "NoSQL", "Хранение данных пользователей: аллергии, предпочтений, истории меню")

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
# Диаграмма компонентов (ML)
![image](https://github.com/user-attachments/assets/d7ac36ff-73b1-483d-a930-aaa76d1b3709)
```PlantUML
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="Microservice\neight sided")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")

SHOW_PERSON_OUTLINE()


    Component(modelEngine, "Model Engine", "Component: ML Core", "Генерирует меню на основе предпочтений пользователя")
    Component(trainingPipeline, "Training Pipeline", "Component: ML Training", "Обучает модели для прогнозирования предпочтений")
    Component(dataPreprocessor, "Data Preprocessor", "Component: Data Processing", "Подготавливает пользовательские параметры для модели")
    Component(recipeFetcher, "Recipe Fetcher", "Component: Integration", "Получает данные о рецептах из внешних источников или баз данных")


ContainerDb(modelDB, "База данных модели", "NoSQL", "Хранение обученных моделей и данных обучения")

Rel(modelEngine, dataPreprocessor, "Получает обработанные данные для расчета меню")
Rel(dataPreprocessor, modelDB, "Читает и сохраняет обработанные данные")
Rel(modelEngine, modelDB, "Использует обученные модели для рекомендаций")
Rel(trainingPipeline, modelDB, "Сохраняет результаты обучения")
Rel(trainingPipeline, dataPreprocessor, "Получает очищенные данные для обучения")
Rel(modelEngine, recipeFetcher, "Получает данные о рецептах")
Rel(recipeFetcher, modelDB, "Читает сохраненные рецепты и ингредиенты")

SHOW_LEGEND()
@enduml
```

Все вместе:
![image](https://github.com/user-attachments/assets/69cf8d94-960d-4903-aede-e6a00a1d1840)
```PlantUML
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="Microservice\neight sided")
AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")

SHOW_PERSON_OUTLINE()

' --- Веб-интерфейс ---
Boundary(webFrontend, "Веб-интерфейс", "Container / React.js") {
    Component(ui, "UI", "Component: Frontend", "Представляет пользовательский интерфейс: ввод параметров, просмотр меню, настройка предпочтений")
    Component(httpClient, "HTTP Client", "Component: Network", "Обрабатывает запросы к API и получение данных")
    Component(router, "Router", "Component: Navigation", "Маршрутизация между страницами приложения")
    Component(stateManager, "State Manager", "Component: State Management", "Управляет состоянием приложения, включая данные пользователя и текущие настройки")
    Component(validation, "Validation Module", "Component: Logic", "Проверяет корректность введенных данных (например, бюджет, предпочтения, аллергии)")
}

Person(user, Пользователь, "Настраивает параметры и получает персональное меню")
Person(admin, Администратор, "Управляет системой и пользователями")
ContainerDb(mongoDB, "MongoDB", "NoSQL", "Хранение данных пользователей: аллергии, предпочтений, истории меню")

Rel(user, ui, "Вводит параметры и просматривает меню")
Rel(admin, ui, "Использует интерфейс для управления системой")
Rel(ui, router, "Навигация между страницами")
Rel(ui, stateManager, "Обновление состояния интерфейса")
Rel(ui, validation, "Проверяет корректность данных")
Rel(validation, stateManager, "Обновляет валидированные данные")
Rel(ui, httpClient, "Отправляет запросы к API")
Rel(stateManager, httpClient, "Передает текущие данные пользователя")
Rel(httpClient, mongoDB, "Читает и записывает данные пользователя")

' --- API Gateway ---
Boundary(apiGateway, "API Gateway", "Container / FastAPI") {
    Component(apiRouter, "Router", "Component: Routing", "Обрабатывает и направляет запросы в соответствующие сервисы")
    Component(authService, "Auth Service", "Component: Security", "Управляет аутентификацией пользователей")
    Component(dataAdapter, "Data Adapter", "Component: Data Layer", "Чтение и запись данных пользователей")
    Component(menuHandler, "Menu Handler", "Component: Logic", "Обрабатывает параметры и запрашивает рекомендации у ML-сервиса")
    Component(logger, "Logger", "Component: Monitoring", "Логирование запросов, ошибок и метрик")
}

Rel(httpClient, apiRouter, "Отправляет запросы на бэкенд")
Rel(apiRouter, authService, "Авторизация запросов")
Rel(apiRouter, dataAdapter, "Запросы к базе данных")
Rel(apiRouter, menuHandler, "Обработка параметров меню")
Rel(apiRouter, logger, "Логирование запросов")
Rel(dataAdapter, mongoDB, "Чтение и запись данных пользователей")
Rel(menuHandler, logger, "Логирование работы с параметрами меню")
Rel(menuHandler, apiRouter, "Возвращает результат обработки")

' --- ML-сервис ---
Boundary(mlService, "ML-сервис", "Container / FastAPI + PyTorch/Scikit-learn") {
    Component(modelEngine, "Model Engine", "Component: ML Core", "Генерирует меню на основе предпочтений пользователя")
    Component(trainingPipeline, "Training Pipeline", "Component: ML Training", "Обучает модели для прогнозирования предпочтений")
    Component(dataPreprocessor, "Data Preprocessor", "Component: Data Processing", "Подготавливает пользовательские параметры для модели")
    Component(recipeFetcher, "Recipe Fetcher", "Component: Integration", "Получает данные о рецептах из внешних источников или баз данных")
}

ContainerDb(modelDB, "База данных модели", "NoSQL", "Хранение обученных моделей и данных обучения")

Rel(menuHandler, modelEngine, "Передает параметры для генерации меню")
Rel(modelEngine, dataPreprocessor, "Получает обработанные данные для расчета меню")
Rel(dataPreprocessor, modelDB, "Читает и сохраняет обработанные данные")
Rel(modelEngine, modelDB, "Использует обученные модели для рекомендаций")
Rel(trainingPipeline, modelDB, "Сохраняет результаты обучения")
Rel(trainingPipeline, dataPreprocessor, "Получает очищенные данные для обучения")
Rel(modelEngine, recipeFetcher, "Получает данные о рецептах")
Rel(recipeFetcher, modelDB, "Читает сохраненные рецепты и ингредиенты")

SHOW_LEGEND()
@enduml
```
