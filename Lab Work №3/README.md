Диаграмма компонентов:
![image](https://github.com/user-attachments/assets/08dd3792-0097-4e56-b876-acf8ff5b5825)

Диаграмма последовательности:
![image](https://github.com/user-attachments/assets/605d8a6d-9ef7-49fa-a8a6-b4b7f27654fb)

Модель БД:
![image](https://github.com/user-attachments/assets/eac1d620-5ae3-4c76-9e9b-e6f5a7e2f74b)

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
Протокол Service в Swift определяет требования для типов, которые должны:

Иметь ассоциированный тип данных T.
Иметь свойство data типа T, доступное для чтения и записи.
Реализовать метод fetchData(id:completion:), который выполняет асинхронную операцию и возвращает результат (или ошибку) через замыкание.
Пример использования: можно создать сервис, который загружает данные (например, строки) асинхронно по идентификатору и возвращает их через замыкание.
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
Класс UserPreferencesService реализует протокол Service, где T — это тип UserPreferences.

Свойство data инициализируется значениями по умолчанию (например, бюджет = 0).
Метод fetchData симулирует загрузку данных предпочтений пользователя (с бюджетом 500, диетой "Vegetarian" и аллергиями на орехи) и передает их через замыкание.
Это пример реализации сервиса, который загружает данные предпочтений пользователя.
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
Класс RecipeRecommendationService реализует протокол Service, где T — это массив рецептов ([Recipe]).

Свойство data инициализируется пустым массивом рецептов.
Метод fetchData симулирует получение рекомендаций рецептов, создавая два рецепта (например, салат и смузи) и передавая их через замыкание.
Это пример сервиса, который предоставляет рекомендации рецептов.
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
В этом коде MainViewController использует сервисы для получения данных:

getUserPreferences:

Инициализирует сервис UserPreferencesService и вызывает метод fetchData для получения предпочтений пользователя.
При успешной загрузке выводит бюджет, диетические предпочтения и аллергии.
getRecipeRecommendations:

Инициализирует сервис RecipeRecommendationService и вызывает метод fetchData для получения рекомендаций рецептов.
При успешной загрузке выводит названия и калории каждого рецепта.
Обе функции обрабатывают результаты через замыкания, включая обработку ошибок.

* **Пояснение учета принципов**  
  а. *KISS (Keep It Simple, Stupid)*  
    -  Простая структура: отдельные сервисы отвечают за конкретные данные (UserPreferences, RecipeRecommendation). Клиентский код взаимодействует через унифицированный интерфейс Service.
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
  
  б. *YAGNI (You Aren't Gonna Need It)*  
    - Реализовано только необходимое: получение пользовательских предпочтений и рекомендаций. Нет ненужных функций или интерфейсов, не требуемых текущей задачей.
      
  в. *DRY (Don't Repeat Yourself)*  
    - Общий протокол Service используется для всех сервисов, минимизируя дублирование. Обработка результата (completion) унифицирована.
```Swift
protocol Service {
    associatedtype T
    var data: T { get set }
    func fetchData(id: Any, completion: @escaping (T?, Error?) -> Void)
}
```
      
  г. *SOLID*  
    - S: Классы имеют четкую единственную ответственность: UserPreferencesService для предпочтений, RecipeRecommendationService для рекомендаций
    - O: Добавление нового типа сервиса (например, для управления логами) возможно без изменения существующего кода, реализуя Service.
    - L: Нет нарушения подстановки, так как клиенты работают с абстрактным протоколом Service.
    - I: Протокол Service содержит только необходимые методы.
    - D: Контроллер MainViewController зависит от абстракции Service, а не от конкретных реализаций.
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
