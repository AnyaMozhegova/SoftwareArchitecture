Диаграмма компонентов:
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
Диаграмма последовательности:
![image](https://github.com/user-attachments/assets/605d8a6d-9ef7-49fa-a8a6-b4b7f27654fb)

```PlantUML
@startuml
actor Пользователь as User
participant "UI" as UI
participant "Router" as Router
participant "State Manager" as StateManager
participant "Validation Module" as Validation
participant "HTTP Client" as HttpClient
participant "API Router" as ApiRouter
participant "Auth Service" as AuthService
participant "Data Adapter" as DataAdapter
participant "Menu Handler" as MenuHandler
participant "Logger" as Logger
database "MongoDB" as MongoDB
participant "Model Engine" as ModelEngine
participant "Data Preprocessor" as DataPreprocessor
database "Model DB" as ModelDB
participant "Recipe Fetcher" as RecipeFetcher

User -> UI: Ввод параметров (предпочтения, аллергии, бюджет)
activate UI
UI -> Validation: Проверка корректности данных
activate Validation
Validation -> UI: Данные валидированы
deactivate Validation

UI -> StateManager: Обновление состояния
activate StateManager
StateManager -> HttpClient: Отправка валидированных данных
activate HttpClient

HttpClient -> ApiRouter: Отправка запроса на обработку меню
activate ApiRouter
ApiRouter -> AuthService: Авторизация запроса
activate AuthService
AuthService -> ApiRouter: Авторизация успешна
deactivate AuthService

ApiRouter -> MenuHandler: Обработка параметров меню
activate MenuHandler
MenuHandler -> Logger: Логирование параметров меню
activate Logger
Logger -> MenuHandler: Логирование завершено
deactivate Logger

MenuHandler -> ModelEngine: Передача параметров для генерации меню
activate ModelEngine
ModelEngine -> DataPreprocessor: Подготовка данных для модели
activate DataPreprocessor
DataPreprocessor -> ModelDB: Получение очищенных данных
activate ModelDB
ModelDB --> DataPreprocessor: Возврат обработанных данных
deactivate ModelDB
deactivate DataPreprocessor

ModelEngine -> RecipeFetcher: Получение рецептов
activate RecipeFetcher
RecipeFetcher -> ModelDB: Чтение данных о рецептах
activate ModelDB
ModelDB --> RecipeFetcher: Рецепты получены
deactivate ModelDB
RecipeFetcher --> ModelEngine: Возврат рецептов
deactivate RecipeFetcher

ModelEngine --> MenuHandler: Возвращение сгенерированного меню
deactivate ModelEngine

MenuHandler -> Logger: Логирование результата обработки
activate Logger
Logger --> MenuHandler: Логирование завершено
deactivate Logger

MenuHandler --> ApiRouter: Результат обработки
deactivate MenuHandler

ApiRouter --> HttpClient: Возврат сгенерированного меню
deactivate ApiRouter

HttpClient --> StateManager: Обновление данных пользователя
deactivate HttpClient

StateManager --> UI: Отображение сгенерированного меню
deactivate StateManager

UI --> User: Показ персонального меню
deactivate UI
@enduml
```
Модель БД:
![image](https://github.com/user-attachments/assets/eac1d620-5ae3-4c76-9e9b-e6f5a7e2f74b)
```PlantUML
@startuml

' Таблица пользователей
class User {
  +id: int
  -username: string
  -password: string
  -isAdmin: boolean
  -preferences: string
  -allergies: string
  -history: string
}

' Таблица рецептов
class Recipe {
  +id: int
  -name: string
  -description: string
  -ingredients: string
  -calories: double
  -tags: string
}

' Таблица параметров пользователя
class UserPreferences {
  +id: int
  -userId: int
  -budget: double
  -dietaryPreferences: string
  -allergies: string
  -createdAt: datetime
}

' Таблица логов запросов
class RequestLog {
  +id: int
  -userId: int
  -timestamp: datetime
  -action: string
  -status: string
  -responseTime: double
}


' Таблица результатов рекомендаций
class MenuRecommendation {
  +id: int
  -userId: int
  -generatedAt: datetime
  -menuItems: string
  -calories: double
}

' Связи между таблицами
User "1" -- "*" UserPreferences: Has
User "1" -- "*" RequestLog: Makes
User "1" -- "*" MenuRecommendation: Receives
MenuRecommendation "1" -- "*" Recipe: Contains


@enduml
```
Описание:
* User — таблица для хранения данных пользователей, включая их предпочтения, аллергии, историю действий.
* Recipe — таблица с информацией о рецептах, включая ингредиенты, калорийность и теги.
* UserPreferences — хранит параметры, которые пользователь вводит (бюджет, предпочтения, аллергии).
* RequestLog — журнал для записи всех действий пользователя с указанием статуса и времени выполнения.
* MenuRecommendation — хранит результаты, сгенерированные системой для пользователя, включая состав меню и общую калорийность.

Эта структура оптимизирована для обеспечения совместимости с описанной выше диаграммой последовательности и компонентов.

Код с учетом принципов KISS, YAGNI, DRY и SOLID
* Модель данных
```Swift
struct UserPreferences {
    let budget: Double
    let dietaryPreferences: [String]
    let allergies: [String]
}

struct Recipe {
    let id: Int
    let name: String
    let description: String
    let calories: Double
    let ingredients: [String]
}
```
* Протокол сервиса
```Swift
protocol Service {
    associatedtype T
    var data: T { get set }
    func fetchData(id: Any, completion: @escaping (T?, Error?) -> Void)
}
```
* Сервис UserPreferencesService
```Swift
class UserPreferencesService: Service {
    typealias T = UserPreferences
    var data: UserPreferences = UserPreferences(budget: 0, dietaryPreferences: [], allergies: [])
    
    func fetchData(id: Any, completion: @escaping (UserPreferences?, Error?) -> Void) {
        // Симуляция загрузки предпочтений
        let preferences = UserPreferences(budget: 500, dietaryPreferences: ["Vegetarian"], allergies: ["Nuts"])
        completion(preferences, nil)
    }
}

```
* Сервис RecipeRecommendationService
```Swift
class RecipeRecommendationService: Service {
    typealias T = [Recipe]
    var data: [Recipe] = []
    
    func fetchData(id: Any, completion: @escaping ([Recipe]?, Error?) -> Void) {
        // Симуляция получения рекомендаций
        let recipes = [
            Recipe(id: 1, name: "Vegetarian Salad", description: "Fresh salad with vegetables", calories: 200, ingredients: ["Lettuce", "Tomatoes"]),
            Recipe(id: 2, name: "Fruit Smoothie", description: "Delicious smoothie with berries", calories: 150, ingredients: ["Berries", "Yogurt"])
        ]
        completion(recipes, nil)
    }
}
```
* Основной контроллер
```Swift
import UIKit

class MainViewController: UIViewController {
    var service: (any Service)?
    let userId = 123
    
    func getUserPreferences() {
        service = UserPreferencesService()
        
        service?.fetchData(id: userId) { (preferences, error) in
            if let preferences = preferences {
                print("Budget: \(preferences.budget)")
                print("Dietary Preferences: \(preferences.dietaryPreferences)")
                print("Allergies: \(preferences.allergies)")
                // Можно сохранить или обработать данные
            } else if let error = error {
                print("Error fetching preferences: \(error.localizedDescription)")
            }
        }
    }
    
    func getRecipeRecommendations() {
        service = RecipeRecommendationService()
        
        service?.fetchData(id: userId) { (recipes, error) in
            if let recipes = recipes {
                for recipe in recipes {
                    print("Recipe: \(recipe.name), Calories: \(recipe.calories)")
                }
            } else if let error = error {
                print("Error fetching recipes: \(error.localizedDescription)")
            }
        }
    }
}
```
* **Пояснение учета принципов**  
  а. *KISS (Keep It Simple, Stupid)*  
    -  Простая структура: отдельные сервисы отвечают за конкретные данные (UserPreferences, RecipeRecommendation). Клиентский код взаимодействует через унифицированный интерфейс Service.
  
  б. *YAGNI (You Aren't Gonna Need It)*  
    - Реализовано только необходимое: получение пользовательских предпочтений и рекомендаций. Нет ненужных функций или интерфейсов, не требуемых текущей задачей.
      
  в. *DRY (Don't Repeat Yourself)*  
    - Общий протокол Service используется для всех сервисов, минимизируя дублирование. Обработка результата (completion) унифицирована.
      
  г. *DRY (Don't Repeat Yourself)*  
    - S: Классы имеют четкую единственную ответственность: UserPreferencesService для предпочтений, RecipeRecommendationService для рекомендаций.
    - O: Добавление нового типа сервиса (например, для управления логами) возможно без изменения существующего кода, реализуя Service.
    - L: Нет нарушения подстановки, так как клиенты работают с абстрактным протоколом Service.
    - I: Протокол Service содержит только необходимые методы.
    - D: Контроллер MainViewController зависит от абстракции Service, а не от конкретных реализаций.
      
Этот код легко поддерживать, расширять, и он соответствует принципам хорошего проектирования.

* **Повышенная сложность**
## BDUF - Big design up front (Масштабное проектирование прежде всего)

**Применимость:** BDUF может быть полезен в проектах с четко определенными требованиями, где изменения маловероятны. Масштабное проектирование на ранних этапах позволяет учесть сложные зависимости между компонентами и избежать необходимости серьезных переработок в будущем.

**Отказ:** Современные гибкие методологии, такие как Agile, часто предполагают итеративный подход к разработке, где требования уточняются на протяжении всего проекта. Использование BDUF может привести к трате времени на проработку деталей, которые позже окажутся ненужными, особенно если проект подвержен изменениям.

**Проект:** Для текущего проекта принцип BDUF ограниченно применим, так как требования четко определены и мало подвержены изменениям. Однако строгого следования принципу не требуется, так как проект ограничен во времени и ресурсах, а также сфокусирован на ключевых функциях. 

## SoC (Separation of concerns — Принцип разделения ответственности)

**Применимость:** Принцип SoC помогает разделить проект на отдельные компоненты с четкими обязанностями. Это способствует улучшению читаемости, тестируемости и повторного использования кода. Например, разделение сервисов (для работы с маршрутами, точками интереса, пользовательскими данными) позволяет облегчить поддержку и тестирование.

**Отказ:** Чрезмерное применение SoC в простых проектах может усложнить архитектуру, привести к избыточности интерфейсов и классов, что будет затруднять работу, особенно если масштаб проекта небольшой.

**Проект:** Принцип SoC применим для данного проекта, так как он уже используется. Например, маршруты, точки интереса и пользовательские предпочтения обрабатываются отдельными сервисами. Это соответствует подходу SoC и облегчает поддержку проекта.

 
## MVP (Minimum viable product — Минимально жизнеспособный продукт)

**Применимость:** MVP позволяет сосредоточиться на разработке минимального набора функций, которые обеспечивают основные потребности пользователей. Это помогает быстро получить обратную связь и внести изменения, если это необходимо. В проектах с ограниченным временем MVP особенно полезен, так как позволяет сконцентрироваться на самом важном.

**Отказ:** Для проектов с высокой технической сложностью может быть необходим более тщательный анализ или прототипирование до создания MVP. Если продукт разрабатывается для узкоопределенной задачи, создание MVP может быть неоправданным.

**Проект:** Для текущего проекта использование принципа MVP целесообразно, так как время ограничено, а конечная цель — продемонстрировать базовую функциональность (работа с маршрутами и предпочтениями пользователя). Это ускоряет процесс и упрощает управление проектом.

## PoC (Proof of concept — Доказательство концепции)

**Применимость:** PoC используется для проверки технической осуществимости определенной идеи или концепции до полноценной разработки. Это помогает снизить риски в проектах, где неизвестна реализация сложных компонентов или технологий. Например, если бы AR-компоненты были ключевой частью проекта, можно было бы провести PoC для проверки их работы.

**Отказ:** Если требования хорошо изучены, PoC может быть избыточным и замедлить процесс разработки. В проектах с ясной архитектурой, где используются стандартные технологии, необходимость в PoC минимальна.

**Проект:** В рамках данного проекта PoC избыточен, так как требования и архитектура ясны, а технологии (сервисы, обработка данных) стандартные. Сжатые сроки и четкая цель делают PoC неоправданным.
