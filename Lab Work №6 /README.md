
# Шаблоны проектирования Gang of Four (GoF)

## Порождающие шаблоны

### Фабричный метод / Factory Method

**Назначение:**  
Определяет интерфейс для создания объекта, но оставляет подклассам решение о том, какой класс инстанцировать. Фабричный метод позволяет создавать объекты без явного указания их типа в коде, а делегирует создание объектов подклассам. Это полезно, когда нужно создавать разные варианты объектов, но при этом скрыть логику создания объекта за фабричным методом.

Каждый раз, когда мы хотим создать нового пользователя, мы используем фабрику. Главное преимущество этого подхода — код клиента не зависит от конкретных классов пользователей, а использует интерфейс фабрики, что позволяет легко добавлять новые типы пользователей в будущем без изменения клиентского кода.

**Пример:**  
Есть интерфейс User, и несколько типов пользователей, например, AdminUser и RegularUser. Мы создадим фабрику для создания этих пользователей.

Cоздаём общий интерфейс User, который будет описывать базовые методы для всех типов пользователей.

Далее создаём два класса: AdminUser и RegularUser, которые реализуют этот интерфейс, но с разной логикой (например, администраторам нужно регистрировать дополнительные права).

Затем создаём интерфейс фабрики пользователей UserFactory, который будет иметь метод createUser(). Каждая фабрика будет создавать конкретные объекты — например, AdminUserFactory для администраторов и RegularUserFactory для обычных пользователей.

UML диаграмма:
Продукт (Product): Определяет интерфейс объектов, которые создаются фабричным методом. это User.

Конкретные продукты (Concrete Products):Реализации интерфейса продукта. это AdminUser и RegularUser.

Создатель (Creator): Определяет фабричный метод для создания объектов. это UserFactory.

Конкретные создатели (Concrete Creators):Реализуют фабричный метод для создания конкретных продуктов. это AdminUserFactory и RegularUserFactory.


![image](https://github.com/user-attachments/assets/a6d62fcd-98f6-4ae4-98d4-b11eaa682dbe)

Код:
```Swift
protocol User {
    func register()
}

class AdminUser: User {
    func register() {
        print("Admin user registered")
    }
}

class RegularUser: User {
    func register() {
        print("Regular user registered")
    }
}

protocol UserFactory {
    func createUser() -> User
}

class AdminUserFactory: UserFactory {
    func createUser() -> User {
        return AdminUser()
    }
}

class RegularUserFactory: UserFactory {
    func createUser() -> User {
        return RegularUser()
    }
}

// Пример использования
let adminFactory: UserFactory = AdminUserFactory()
let adminUser: User = adminFactory.createUser()
adminUser.register()

let regularFactory: UserFactory = RegularUserFactory()
let regularUser: User = regularFactory.createUser()
regularUser.register()
```
### Абстрактная фабрика / Abstract Factory

**Назначение:**  
Абстрактная фабрика предоставляет интерфейс для создания семейств связанных объектов, не указывая их конкретные классы. Этот паттерн полезен, когда нужно создавать целые группы объектов, которые должны работать вместе (например, рюкзаки и палатки для туристов).

**Пример:**  
Представим, что для разных типов пользователей (например, веганов и обычных людей) мы хотим создать соответствующие предпочтения и меню. Для этого:

Создадим интерфейсы UserPreferences и Menu.

Определим конкретные реализации предпочтений и меню для веганов (VeganPreferences, VeganMenu) и обычных пользователей (RegularPreferences, RegularMenu).

Затем создадим интерфейс абстрактной фабрики UserEquipmentFactory, который будет создавать эти объекты. Каждая конкретная фабрика будет создавать соответствующие предпочтения и меню для каждого типа пользователя.

**Пояснение:** 
В отличие от фабричного метода, где мы создаём один объект, абстрактная фабрика позволяет создать несколько объектов, которые работают в связке (например, рюкзак и палатка).

Используя абстрактную фабрику, клиентский код не зависит от того, какие конкретно объекты создаются. Мы просто указываем фабрику, и она сама создаёт нужные объекты.

UML диаграмма:
Абстрактные продукты (Abstract Products):

Определяют интерфейсы для типов продуктов, которые будут создаваться фабрикой. это UserPreferences и Menu.

Конкретные продукты (Concrete Products):Реализации абстрактных продуктов для конкретных семейств. это VeganPreferences, RegularPreferences, VeganMenu, RegularMenu.

Абстрактная фабрика (Abstract Factory):Определяет интерфейс для создания семейства продуктов. это UserEquipmentFactory.

Конкретные фабрики (Concrete Factories):Реализуют методы абстрактной фабрики для создания конкретных продуктов.это VeganUserFactory и RegularUserFactory.

![image](https://github.com/user-attachments/assets/98ceea1e-9ab6-42cb-b8f8-2dc0003976e1)

Код:
```Swift
protocol UserPreferences {
    func setPreferences()
}

protocol Menu {
    func createMenu()
}

class VeganPreferences: UserPreferences {
    func setPreferences() {
        print("Setting vegan preferences")
    }
}

class RegularPreferences: UserPreferences {
    func setPreferences() {
        print("Setting regular preferences")
    }
}

class VeganMenu: Menu {
    func createMenu() {
        print("Creating vegan menu")
    }
}

class RegularMenu: Menu {
    func createMenu() {
        print("Creating regular menu")
    }
}

protocol UserEquipmentFactory {
    func createPreferences() -> UserPreferences
    func createMenu() -> Menu
}

class VeganUserFactory: UserEquipmentFactory {
    func createPreferences() -> UserPreferences {
        return VeganPreferences()
    }
    
    func createMenu() -> Menu {
        return VeganMenu()
    }
}

class RegularUserFactory: UserEquipmentFactory {
    func createPreferences() -> UserPreferences {
        return RegularPreferences()
    }
    
    func createMenu() -> Menu {
        return RegularMenu()
    }
}

// Пример использования
let veganFactory: UserEquipmentFactory = VeganUserFactory()
let veganPreferences = veganFactory.createPreferences()
veganPreferences.setPreferences()
let veganMenu = veganFactory.createMenu()
veganMenu.createMenu()

let regularFactory: UserEquipmentFactory = RegularUserFactory()
let regularPreferences = regularFactory.createPreferences()
regularPreferences.setPreferences()
let regularMenu = regularFactory.createMenu()
regularMenu.createMenu()
```

### Одиночка / Singleton

**Назначение:** 
Одиночка гарантирует, что у класса будет только один экземпляр, и предоставляет к нему глобальную точку доступа. Это полезно для управления состоянием в приложении, где должен быть только один объект, например, для центра авторизации или логирования.

**Пример:**
Предположим, у нас есть класс AuthorizationManager, который управляет авторизацией пользователей. Мы хотим гарантировать, что в системе будет только один экземпляр этого класса.

Для этого создаём статическую переменную shared, которая будет хранить единственный экземпляр класса.
Инициализатор класса приватный, чтобы другие объекты не могли создать новый экземпляр.
Мы используем статический метод shared, чтобы получить доступ к этому экземпляру.

Пояснение:
Паттерн Одиночка решает проблему создания единственного объекта, например, для управления настройками, авторизацией или логированием в приложении. Использование этого паттерна гарантирует, что в любой момент времени будет только один экземпляр класса, что упрощает управление состоянием.

UML диаграмма:
Статический экземпляр:Единственный экземпляр класса, который хранится в статической переменной. это static let shared = AuthorizationManager().

Приватный инициализатор:Предотвращает создание новых экземпляров класса извне. это private init().

Глобальная точка доступа:Метод или свойство, через которое можно получить доступ к единственному экземпляру класса.это AuthorizationManager.shared.


![image](https://github.com/user-attachments/assets/eb7bd34a-af92-4a19-9fd2-9c156a6bdb77)

Код:
```Swift
class AuthorizationManager {
    static let shared = AuthorizationManager()  // Единственный экземпляр

    private init() {
        // Приватный инициализатор, чтобы предотвратить создание других экземпляров
    }

    func authorizeUser() {
        print("Authorizing user")  // Логика авторизации
    }
}

// Пример использования
let authManager1 = AuthorizationManager.shared  // Получаем единственный экземпляр
let authManager2 = AuthorizationManager.shared  // Получаем тот же экземпляр

authManager1.authorizeUser()  // Авторизуем пользователя
authManager2.authorizeUser()  // Тот же экземпляр, снова авторизуем

print(authManager1 === authManager2)  // true, это один и тот же экземпляр
```
## Структурные шаблоны

### Адаптер / Adapter

**Назначение:** 
Паттерн "Адаптер" используется для преобразования интерфейса одного класса в другой интерфейс, который ожидает клиент. Это полезно, когда у вас есть класс с несовместимым интерфейсом, и вам нужно использовать его в рамках существующей системы.

**Пример:**
Интеграция с внешним API для рецептов
Есть внешний API для получения рецептов, но его интерфейс отличается от того, который используется в вашем приложении. Для интеграции с этим сервисом мы создаем адаптер, который приведет внешний интерфейс к ожидаемому.

Проблема: У нас есть класс ExternalRecipeAPI, который получает рецепты в виде строк. Однако в вашем приложении ожидается массив объектов типа Recipe.
Решение: Используем адаптер для преобразования строковых данных в объекты Recipe.

![image](https://github.com/user-attachments/assets/f504d519-c8b7-4408-ab05-ef727ff4c9ec)

Код:
```Swift
// Протокол, который мы ожидаем
protocol RecipeService {
    func fetchRecipes(completion: @escaping ([Recipe]?, Error?) -> Void)
}

// Внешний сервис с другим интерфейсом
class ExternalRecipeAPI {
    func getRecipesFromAPI(completion: @escaping ([String]?, Error?) -> Void) {
        // Имитация запроса к внешнему API
        completion(["Recipe 1", "Recipe 2"], nil)
    }
}

// Адаптер, который преобразует интерфейс внешнего API в тот, который нам нужен
class RecipeServiceAdapter: RecipeService {
    private let externalAPI: ExternalRecipeAPI
    
    init(externalAPI: ExternalRecipeAPI) {
        self.externalAPI = externalAPI
    }
    
    func fetchRecipes(completion: @escaping ([Recipe]?, Error?) -> Void) {
        externalAPI.getRecipesFromAPI { recipeNames, error in
            if let recipeNames = recipeNames {
                // Преобразуем строки в объекты Recipe
                let recipes = recipeNames.map { Recipe(name: $0, calories: 200) }
                completion(recipes, nil)
            } else {
                completion(nil, error)
            }
        }
    }
}
```
### Мост / Bridge

**Назначение:** 
Паттерн "Мост" позволяет разделить абстракцию и её реализацию, чтобы они могли изменяться независимо друг от друга. Это полезно, когда у вас есть несколько абстракций и разных реализаций, которые нужно сочетать.

**Пример:**
Рекомендации на основе различных факторов (бюджет, диетические предпочтения)
Предположим, у нас есть система рекомендаций, которая может генерировать рецепты на основе различных критериев, таких как бюджет или диетические предпочтения. С помощью паттерна "Мост" можно разделить абстракцию от конкретных реализаций, чтобы каждый компонент мог развиваться независимо.

Проблема: У нас есть несколько типов рекомендаций, которые должны использовать одну абстракцию.
Решение: Используем паттерн "Мост", чтобы разделить абстракцию генерации рекомендаций от конкретной логики.

![image](https://github.com/user-attachments/assets/3d29d6f6-e8df-415b-b411-d42791c108af)

Код:
```Swift
// Абстракция для рекомендации
protocol Recommendation {
    func generateRecommendations() -> [Recipe]
}

// Реализация для рекомендаций по бюджету
class BudgetRecommendation: Recommendation {
    private let userPreferences: UserPreferences
    
    init(userPreferences: UserPreferences) {
        self.userPreferences = userPreferences
    }
    
    func generateRecommendations() -> [Recipe] {
        // Логика рекомендаций на основе бюджета
        return [Recipe(name: "Budget Recipe", calories: 150)]
    }
}

// Реализация для рекомендаций по диетическим предпочтениям
class DietaryRecommendation: Recommendation {
    private let userPreferences: UserPreferences
    
    init(userPreferences: UserPreferences) {
        self.userPreferences = userPreferences
    }
    
    func generateRecommendations() -> [Recipe] {
        // Логика рекомендаций на основе диетических предпочтений
        return [Recipe(name: "Vegetarian Recipe", calories: 300)]
    }
}

// Пример использования
let userPreferences = UserPreferences(budget: 500, dietaryPreferences: ["Vegetarian"], allergies: ["Nuts"])
let recommendation = DietaryRecommendation(userPreferences: userPreferences)

let recipes = recommendation.generateRecommendations()
```
### Декоратор / Decorator

**Назначение:**
Паттерн "Декоратор" используется для динамического добавления нового функционала объектам. Это позволяет изменить поведение объекта на лету, не изменяя его исходный код.

**Пример:**
Фильтрация рецептов по аллергии
Предположим, что  нужно добавить фильтрацию рецептов на основе аллергенов. Вместо того, чтобы изменять основной код, вы можете использовать паттерн "Декоратор", чтобы обогатить функциональность без изменения исходного класса.

Проблема: Мы хотим добавить возможность фильтрации рецептов по аллергиям.
Решение: Создаем декоратор, который будет фильтровать рецепты, добавляя это поведение к уже существующему объекту.

![image](https://github.com/user-attachments/assets/a685a0d5-c4a2-4ba5-be0b-5e7f2e52405e)

Код:
```Swift
// Протокол для предоставления рецептов
protocol RecipeProvider {
    func getRecipes() -> [Recipe]
}

// Реализация для получения базовых рецептов
class SimpleRecipeProvider: RecipeProvider {
    func getRecipes() -> [Recipe] {
        return [Recipe(name: "Recipe 1", calories: 200), Recipe(name: "Recipe 2", calories: 300)]
    }
}

// Декоратор для фильтрации по аллергии
class AllergyFilterDecorator: RecipeProvider {
    private let decoratedProvider: RecipeProvider
    private let allergies: [String]
    
    init(decoratedProvider: RecipeProvider, allergies: [String]) {
        self.decoratedProvider = decoratedProvider
        self.allergies = allergies
    }
    
    func getRecipes() -> [Recipe] {
        let allRecipes = decoratedProvider.getRecipes()
        return allRecipes.filter { recipe in
            !self.allergies.contains(where: { recipe.name.contains($0) })
        }
    }
}

// Пример использования
let simpleProvider = SimpleRecipeProvider()
let allergyFilteredProvider = AllergyFilterDecorator(decoratedProvider: simpleProvider, allergies: ["Nuts"])

let filteredRecipes = allergyFilteredProvider.getRecipes()
```

### Компоновщик  / Composite

**Назначение:**
Паттерн "Компоновщик" используется для создания иерархий объектов, которые обрабатываются одинаково, независимо от того, являются ли они "простыми" объектами или "составными". Это позволяет строить сложные объекты из простых компонентов.

**Пример:**
Меню, состоящее из разных рецептов
Предположим, вам нужно реализовать меню, которое может включать как простые рецепты, так и группы рецептов. Паттерн "Компоновщик" позволит вам обрабатывать все эти элементы одинаково.

Проблема: Нужно объединить рецепты в группы и работать с ними как с единым объектом.
Решение: Создаем интерфейс MenuItem для всех элементов меню, а затем используем классы, которые могут быть как одиночными рецепты, так и коллекциями рецептов.

![image](https://github.com/user-attachments/assets/1110f325-0486-4bb9-9c79-f2032a3bdd32)

Код:
```Swift
// Протокол для всех элементов меню
protocol MenuItem {
    func getDescription() -> String
}

// Простое меню с одним рецептом
class RecipeMenuItem: MenuItem {
    private let name: String
    
    init(name: String) {
        self.name = name
    }
    
    func getDescription() -> String {
        return name
    }
}

// Составное меню, которое может содержать другие элементы меню
class MenuCollection: MenuItem {
    private var items: [MenuItem] = []
    
    func addItem(item: MenuItem) {
        items.append(item)
    }
    
    func getDescription() -> String {
        return items.map { $0.getDescription() }.joined(separator: ", ")
    }
}

// Пример использования
let recipe1 = RecipeMenuItem(name: "Recipe 1")
let recipe2 = RecipeMenuItem(name: "Recipe 2")
let menu = MenuCollection()
menu.addItem(item: recipe1)
menu.addItem(item: recipe2)

print(menu.getDescription())  // Выводит: "Recipe 1, Recipe 2"
```

## Поведенческие шаблоны

### Стратегия / Strategy
**Назначение:**  
Паттерн "Стратегия" определяет семейство алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми. Это позволяет изменять алгоритмы независимо от клиентов, которые ими пользуются.

**Пример:**
"Стратегия" может использоваться для выбора различных алгоритмов рекомендации рецептов в зависимости от предпочтений пользователя. Например, можно реализовать стратегии подбора рецептов с учетом бюджета, аллергий и калорийности.

![image](https://github.com/user-attachments/assets/2789b278-9e8f-4f5b-a894-d6eff7bd53db)


Код:
```Swift
protocol RecommendationStrategy {
    func recommendRecipes(for user: User) -> [Recipe]
}

class BudgetBasedStrategy: RecommendationStrategy {
    func recommendRecipes(for user: User) -> [Recipe] {
        return RecipeDatabase.shared.recipes.filter { $0.price <= user.preferences.budget }
    }
}

class AllergyAwareStrategy: RecommendationStrategy {
    func recommendRecipes(for user: User) -> [Recipe] {
        return RecipeDatabase.shared.recipes.filter { recipe in
            !recipe.ingredients.contains(where: { user.preferences.allergies.contains($0) })
        }
    }
}

class CalorieBasedStrategy: RecommendationStrategy {
    func recommendRecipes(for user: User) -> [Recipe] {
        return RecipeDatabase.shared.recipes.filter { $0.calories <= user.preferences.calorieLimit }
    }
}

class RecipeRecommender {
    private var strategy: RecommendationStrategy
    
    init(strategy: RecommendationStrategy) {
        self.strategy = strategy
    }
    
    func setStrategy(_ strategy: RecommendationStrategy) {
        self.strategy = strategy
    }
    
    func getRecommendations(for user: User) -> [Recipe] {
        return strategy.recommendRecipes(for: user)
    }
}
```
### Наблюдатель  / Observer

**Назначение:**  
Определяет зависимость "один ко многим" между объектами так, что при изменении состояния одного объекта все зависимые объекты автоматически получают уведомление и обновляются.

**Пример:**  
Паттерн "Наблюдатель" используется для обновления рекомендаций меню, когда пользователь изменяет свои предпочтения (например, добавляет аллергию или меняет бюджет).

![image](https://github.com/user-attachments/assets/a3602f92-43ae-47b6-9a36-72081bf7e923)

Код:
```Swift
protocol UserPreferencesObserver: AnyObject {
    func updatePreferences(for user: User)
}

class UserPreferencesSubject {
    private var observers: [UserPreferencesObserver] = []
    
    func addObserver(observer: UserPreferencesObserver) {
        observers.append(observer)
    }
    
    func removeObserver(observer: UserPreferencesObserver) {
        observers.removeAll { $0 === observer }
    }
    
    func notifyObservers(user: User) {
        for observer in observers {
            observer.updatePreferences(for: user)
        }
    }
}
```

### Состояние  / State

**Назначение:**  
Позволяет объекту изменять свое поведение в зависимости от внутреннего состояния.

**Пример:** 
Паттерн "Состояние" может использоваться для изменения поведения системы в зависимости от уровня активности пользователя (например, новый пользователь, активный пользователь, редко использующий сервис).

![image](https://github.com/user-attachments/assets/0ca78bb3-9956-4d17-aa5b-bd37c49bddcb)

Код:
```Swift
class UserState {
    func handle() {
        // Базовая реализация
    }
}

class NewUserState: UserState {
    override func handle() {
        print("Отображаем приветственное сообщение")
    }
}

class ActiveUserState: UserState {
    override func handle() {
        print("Показываем новые рекомендации")
    }
}

class InactiveUserState: UserState {
    override func handle() {
        print("Отправляем напоминание пользователю")
    }
}

class UserContext {
    private var state: UserState
    
    init(initialState: UserState) {
        self.state = initialState
    }
    
    func setState(newState: UserState) {
        self.state = newState
    }
    
    func requestState() {
        self.state.handle()
    }
}
```

### Команда   / Command

**Назначение:**  
Паттерн Command позволяет инкапсулировать запрос пользователя в виде отдельного объекта. Это полезно в случаях, когда необходимо:

Логировать действия пользователей (например, запрос на рекомендации или обновление предпочтений).

Позволять откат или повторное выполнение действий.

Организовать очередь команд для последовательного выполнения.

**Пример:** 
журнал RequestLog, который хранит все запросы пользователей. Использование паттерна "Команда" позволит:

Представить каждое действие пользователя в виде объекта команды.

Централизованно логировать выполнение команд в RequestLog.

Упростить поддержку кода за счет разделения логики выполнения и логирования.

UserActionCommand — общий интерфейс для всех команд.

GetRecommendationsCommand — команда для получения рекомендаций.

UpdatePreferencesCommand — команда для обновления предпочтений.

RequestLogger — обработчик команд, записывающий их в журнал RequestLog перед выполнением.

![image](https://github.com/user-attachments/assets/575c197c-2cdd-449b-9667-a5aadd52e01d)

Код:
```Swift
import Foundation

// Протокол команды
protocol UserActionCommand {
    func execute()
}

// Команда для получения рекомендаций
class GetRecommendationsCommand: UserActionCommand {
    private let userId: Int

    init(userId: Int) {
        self.userId = userId
    }

    func execute() {
        print("Получение рекомендаций для пользователя с ID \(userId)")
        // Вызов сервиса рекомендаций
        let service = RecipeRecommendationService()
        service.fetchData(id: userId) { recipes, error in
            if let recipes = recipes {
                print("Рекомендации: \(recipes.map { $0.name }.joined(separator: ", "))")
            } else if let error = error {
                print("Ошибка получения рекомендаций: \(error.localizedDescription)")
            }
        }
    }
}

// Команда для обновления предпочтений пользователя
class UpdatePreferencesCommand: UserActionCommand {
    private let userId: Int
    private let newPreferences: UserPreferences

    init(userId: Int, newPreferences: UserPreferences) {
        self.userId = userId
        self.newPreferences = newPreferences
    }

    func execute() {
        print("Обновление предпочтений пользователя с ID \(userId)")
        // Здесь можно вызвать сервис обновления предпочтений
    }
}

// Логгер запросов
class RequestLogger {
    func executeCommand(command: UserActionCommand) {
        print("Логирование команды: \(type(of: command))")
        command.execute()
    }
}

// Использование команд
let logger = RequestLogger()
let getRecommendations = GetRecommendationsCommand(userId: 123)
let updatePreferences = UpdatePreferencesCommand(userId: 123, newPreferences: UserPreferences(budget: 1000, dietaryPreferences: ["Vegan"], allergies: ["Dairy"]))

logger.executeCommand(command: getRecommendations)
logger.executeCommand(command: updatePreferences)
```

### Шаблонный метод  / Template Method

**Назначение:**  
Паттерн Template Method определяет общую структуру алгоритма, позволяя подклассам изменять отдельные шаги.


**Пример:** 
Система генерирует рекомендации на основе предпочтений пользователя. Этот процесс можно стандартизировать с помощью шаблонного метода:

Определить общий процесс генерации рекомендаций.

Разрешить подклассам изменять конкретные шаги (например, фильтрацию рецептов по разным критериям).

Исключить дублирование кода.

MenuRecommendationTemplate — абстрактный класс, содержащий метод generateMenu(), включающий шаги процесса.
BudgetBasedMenuRecommendation — конкретная реализация, фильтрующая рецепты по бюджету.
DietaryBasedMenuRecommendation — реализация, фильтрующая рецепты по диетическим предпочтениям.

![image](https://github.com/user-attachments/assets/09f0c93d-11a0-46ed-a3ee-10192f642b35)

Код:
```Swift
import Foundation

// Абстрактный класс для генерации меню
class MenuRecommendationTemplate {

    // Шаблонный метод, определяющий процесс генерации меню
    final func generateMenu(userId: Int) {
        let preferences = fetchUserPreferences(userId: userId)
        let recipes = fetchRecipes()
        let filteredRecipes = filterRecipes(recipes: recipes, preferences: preferences)
        createRecommendation(userId: userId, recipes: filteredRecipes)
    }

    // Получение предпочтений пользователя
    func fetchUserPreferences(userId: Int) -> UserPreferences {
        print("Загрузка предпочтений пользователя \(userId)")
        return UserPreferences(budget: 500, dietaryPreferences: ["Vegetarian"], allergies: ["Nuts"])
    }

    // Получение списка рецептов
    func fetchRecipes() -> [Recipe] {
        print("Загрузка списка рецептов")
        return [Recipe(name: "Салат", calories: 200), Recipe(name: "Суп", calories: 300)]
    }

    // Метод для фильтрации рецептов (реализуется в подклассах)
    func filterRecipes(recipes: [Recipe], preferences: UserPreferences) -> [Recipe] {
        fatalError("Этот метод должен быть переопределен в подклассе")
    }

    // Создание меню на основе отфильтрованных рецептов
    func createRecommendation(userId: Int, recipes: [Recipe]) {
        print("Создание меню для пользователя \(userId): \(recipes.map { $0.name }.joined(separator: ", "))")
    }
}

// Реализация с фильтрацией по бюджету
class BudgetBasedMenuRecommendation: MenuRecommendationTemplate {
    override func filterRecipes(recipes: [Recipe], preferences: UserPreferences) -> [Recipe] {
        print("Фильтрация рецептов по бюджету: \(preferences.budget)")
        return recipes.filter { _ in preferences.budget >= 500 }
    }
}

// Реализация с фильтрацией по диетическим предпочтениям
class DietaryBasedMenuRecommendation: MenuRecommendationTemplate {
    override func filterRecipes(recipes: [Recipe], preferences: UserPreferences) -> [Recipe] {
        print("Фильтрация рецептов по диетическим предпочтениям: \(preferences.dietaryPreferences)")
        return recipes.filter { _ in preferences.dietaryPreferences.contains("Vegetarian") }
    }
}

// Использование шаблонного метода
let budgetRecommendation = BudgetBasedMenuRecommendation()
budgetRecommendation.generateMenu(userId: 123)

let dietaryRecommendation = DietaryBasedMenuRecommendation()
dietaryRecommendation.generateMenu(userId: 123)
```
# Шаблоны проектирования GRASP

## Роли

### Information Expert

**Проблема:** информация в системе должна обрабатываться, аккумулироваться,
рассчитываться.

**Решение:** назначить соответствующие обязанности тому классу, который её
содержит
Каждый сервис отвечает за обработку и хранение специфических данных. Например, UserPreferencesService отвечает за пользовательские предпочтения, а RecipeService управляет данными о рецептах.

**Код:** при проектировании синглтона, как раз был создан класс-информатор

```Swift
class UserPreferencesService: Service {
    typealias T = UserPreferences
    var data: UserPreferences = UserPreferences(budget: 0, dietaryPreferences: [], allergies: [])
    
    func fetchData(id: Any, completion: @escaping (UserPreferences?, Error?) -> Void) {
        // Загрузка предпочтений пользователя
        let preferences = UserPreferences(budget: 500, dietaryPreferences: ["Vegetarian"], allergies: ["Nuts"])
        completion(preferences, nil)
    }
}
```
### Creator
**Проблема:** экземпляры класса необходимо создавать

**Решение:** назначить обязанности инстанциирования тому классу, который будет использовать соответствующие экземпляры созданных классов

**Код:** Сервис рекомендаций (MenuRecommendationService) создает объекты рекомендаций (MenuRecommendation), так как он отвечает за их генерацию.

```Swift
class MenuRecommendationService {
    func generateRecommendation(for user: UserPreferences) -> MenuRecommendation {
        let recommendedRecipes = RecipeService().getRecipes(for: user)
        return MenuRecommendation(recipes: recommendedRecipes, totalCalories: recommendedRecipes.reduce(0) { $0 + $1.calories })
    }
}
```

### Controller

**Проблема:** необходимо обрабатывать входные системные события

**Решение:** назначить обязанность обработки входных системных событий специальному классу

**Код:** MainViewController управляет запросами пользователя, передает их в сервисы и обрабатывает результаты.
```Swift
import UIKit

class MainViewController: UIViewController {
    var userService: UserPreferencesService = UserPreferencesService()
    var recommendationService: MenuRecommendationService = MenuRecommendationService()
    let userId = 123

    func getUserPreferences() {
        userService.fetchData(id: userId) { (preferences, error) in
            if let preferences = preferences {
                self.getMenuRecommendation(for: preferences)
            }
        }
    }

    func getMenuRecommendation(for preferences: UserPreferences) {
        let recommendation = recommendationService.generateRecommendation(for: preferences)
        print("Recommended Menu: \(recommendation.recipes.map { $0.name })")
    }
}
```

### Pure Fabrication

**Проблема:** Необходимо обеспечивать Low Coupling (низкую связанность) и High Cohesion (высокую связность) в проекте. Бизнес-логика, связанная с управлением данными (например, загрузка и сохранение пользовательских предпочтений, рецептов), не должна быть смешана с логикой приложения.

**Решение:** назначить обязанность обработки входных системных событий специальному классу

**Код:** Синтезировать искусственную сущность (класс DataManager), которая будет отвечать за управление данными. Это позволит отделить логику работы с данными от бизнес-логики и улучшит структуру системы.
```Swift
// Пример Pure Fabrication - синтезированная сущность для работы с данными
class DataManager {
    // Метод для сохранения предпочтений пользователя
    func saveUserPreferences(_ preferences: UserPreferences) {
        // Логика сохранения предпочтений
        print("User preferences saved: \(preferences)")
    }

    // Метод для загрузки рецептов
    func fetchRecipes(completion: @escaping ([Recipe]?, Error?) -> Void) {
        // Логика загрузки рецептов
        let recipes = [
            Recipe(name: "Vegetarian Salad", calories: 200, ingredients: ["Lettuce", "Tomato", "Cucumber"]),
            Recipe(name: "Chicken Soup", calories: 300, ingredients: ["Chicken", "Carrot", "Potato"])
        ]
        completion(recipes, nil)
    }
}

// Пример использования Pure Fabrication
let dataManager = DataManager()
let userPreferences = UserPreferences(budget: 500, dietaryPreferences: ["Vegetarian"], allergies: ["Nuts"])

dataManager.saveUserPreferences(userPreferences)
dataManager.fetchRecipes { recipes, error in
    if let recipes = recipes {
        print("Recipes loaded: \(recipes)")
    } else if let error = error {
        print("Error loading recipes: \(error.localizedDescription)")
    }
}
```
Связь с другими паттернами:

Facade: DataManager может выступать в роли фасада, предоставляя простой интерфейс для работы с данными.

Strategy: Можно использовать стратегии для изменения способа загрузки или сохранения данных (например, локальное хранилище или облачное).

### Indirection

**Проблема:** Прямая связь между компонентами (например, между MainViewController и сервисами) увеличивает связанность системы, что усложняет её поддержку и расширение.

**Решение:** Использовать промежуточный компонент (RecommendationService), который будет выступать посредником между MainViewController и сервисами. Это уменьшит прямую связь между компонентами.
```Swift
// Пример Indirection - посредник для генерации рекомендаций
class RecommendationService {
    private let userPreferencesService = UserPreferencesService()
    private let recipeService = RecipeService()

    func generateRecommendations(for userId: Int, completion: @escaping ([Recipe]?, Error?) -> Void) {
        userPreferencesService.fetchData(id: userId) { preferences, error in
            if let preferences = preferences {
                self.recipeService.fetchRecipes { recipes, error in
                    if let recipes = recipes {
                        // Фильтрация рецептов на основе предпочтений
                        let filteredRecipes = recipes.filter { recipe in
                            return !preferences.allergies.contains(where: { recipe.ingredients.contains($0) })
                        }
                        completion(filteredRecipes, nil)
                    } else if let error = error {
                        completion(nil, error)
                    }
                }
            } else if let error = error {
                completion(nil, error)
            }
        }
    }
}

// Пример использования Indirection
let recommendationService = RecommendationService()
recommendationService.generateRecommendations(for: 123) { recipes, error in
    if let recipes = recipes {
        print("Recommended recipes: \(recipes)")
    } else if let error = error {
        print("Error generating recommendations: \(error.localizedDescription)")
    }
}
```
Связь с другими паттернами:

Mediator: RecommendationService выступает в роли посредника между сервисами и контроллером.

Facade: Может использоваться для упрощения взаимодействия с несколькими сервисами.

## Принципы разработки

### Low Coupling

**Проблема:** Высокая связанность между классами (например, между MainViewController и сервисами) усложняет тестирование и модификацию системы.

**Решение:** Использовать протоколы для уменьшения связанности. MainViewController будет зависеть от абстракций (UserPreferencesServiceProtocol, RecipeServiceProtocol), а не от конкретных реализаций.
```Swift
// Пример Low Coupling - использование протоколов
protocol UserPreferencesServiceProtocol {
    func fetchData(id: Any, completion: @escaping (UserPreferences?, Error?) -> Void)
}

protocol RecipeServiceProtocol {
    func fetchRecipes(completion: @escaping ([Recipe]?, Error?) -> Void)
}

class MainViewController: UIViewController {
    var userPreferencesService: UserPreferencesServiceProtocol?
    var recipeService: RecipeServiceProtocol?
    let userId = 123

    override func viewDidLoad() {
        super.viewDidLoad()
        userPreferencesService = UserPreferencesService()
        recipeService = RecipeService()
    }

    func getUserPreferences() {
        userPreferencesService?.fetchData(id: userId) { preferences, error in
            if let preferences = preferences {
                print("User Preferences: \(preferences)")
            } else if let error = error {
                print("Error: \(error.localizedDescription)")
            }
        }
    }
}
```
Связь с другими паттернами:

Dependency Injection: Внедрение зависимостей через протоколы.

Adapter: Протоколы могут использоваться для адаптации различных реализаций.

### High Cohesion

**Проблема:** Классы выполняют слишком много задач, что снижает читаемость и поддерживаемость кода.

**Решение:** Разделить ответственности между классами. Каждый класс должен выполнять одну четко определённую задачу.
```Swift
// Пример High Cohesion - разделение ответственностей
class UserPreferencesService: UserPreferencesServiceProtocol {
    func fetchData(id: Any, completion: @escaping (UserPreferences?, Error?) -> Void) {
        // Логика загрузки предпочтений
        let preferences = UserPreferences(budget: 500, dietaryPreferences: ["Vegetarian"], allergies: ["Nuts"])
        completion(preferences, nil)
    }
}

class RecipeService: RecipeServiceProtocol {
    func fetchRecipes(completion: @escaping ([Recipe]?, Error?) -> Void) {
        // Логика загрузки рецептов
        let recipes = [
            Recipe(name: "Vegetarian Salad", calories: 200, ingredients: ["Lettuce", "Tomato", "Cucumber"]),
            Recipe(name: "Chicken Soup", calories: 300, ingredients: ["Chicken", "Carrot", "Potato"])
        ]
        completion(recipes, nil)
    }
}
```
Связь с другими паттернами:

Single Responsibility Principle (SOLID): Каждый класс отвечает за одну задачу.

Facade: Классы могут быть объединены в фасад для упрощения взаимодействия.

### Polymorphism 

**Проблема:** В проекте может возникнуть необходимость работы с разными типами данных (например, пользователи, рецепты, рекомендации) через единый интерфейс. Жесткая привязка к конкретным типам данных усложняет расширение системы и добавление новых функциональностей.

**Решение:** Использовать полиморфизм для работы с разными типами данных через единый интерфейс. Это позволяет системе быть гибкой и поддерживать новые типы данных без изменения существующего кода.

```Swift
// Пример Polymorphism - использование протокола для работы с разными типами данных
protocol Displayable {
    func display() -> String
}

// Реализация для UserPreferences
extension UserPreferences: Displayable {
    func display() -> String {
        return "Budget: \(budget), Preferences: \(dietaryPreferences.joined(separator: ", ")), Allergies: \(allergies.joined(separator: ", "))"
    }
}

// Реализация для Recipe
extension Recipe: Displayable {
    func display() -> String {
        return "Recipe: \(name), Calories: \(calories), Ingredients: \(ingredients.joined(separator: ", "))"
    }
}

// Пример использования полиморфизма
let userPreferences = UserPreferences(budget: 500, dietaryPreferences: ["Vegetarian"], allergies: ["Nuts"])
let recipe = Recipe(name: "Vegetarian Salad", calories: 200, ingredients: ["Lettuce", "Tomato", "Cucumber"])

let items: [Displayable] = [userPreferences, recipe]

for item in items {
    print(item.display())
}
```
Связь с другими паттернами:

Strategy: Полиморфизм может использоваться для реализации различных стратегий (например, разные способы отображения данных).

Adapter: Полиморфизм помогает адаптировать разные типы данных к единому интерфейсу.

## Свойство программы

### Protected Variations 

**Проблема:** Изменения в одной части системы (например, изменение структуры данных или логики работы с данными) могут привести к необходимости изменений в других частях системы. Это увеличивает риск ошибок и усложняет поддержку

**Решение:** Защитить систему от изменений, изолировав изменяющиеся части. Это можно сделать с помощью абстракций (протоколов) и инкапсуляции.

**Код:**
```Swift
// Пример Protected Variations - использование протоколов для защиты от изменений
protocol DataService {
    associatedtype T
    func fetchData(id: Any, completion: @escaping (T?, Error?) -> Void)
}

class UserPreferencesService: DataService {
    typealias T = UserPreferences

    func fetchData(id: Any, completion: @escaping (UserPreferences?, Error?) -> Void) {
        // Логика загрузки предпочтений
        let preferences = UserPreferences(budget: 500, dietaryPreferences: ["Vegetarian"], allergies: ["Nuts"])
        completion(preferences, nil)
    }
}

class RecipeService: DataService {
    typealias T = [Recipe]

    func fetchData(id: Any, completion: @escaping ([Recipe]?, Error?) -> Void) {
        // Логика загрузки рецептов
        let recipes = [
            Recipe(name: "Vegetarian Salad", calories: 200, ingredients: ["Lettuce", "Tomato", "Cucumber"]),
            Recipe(name: "Chicken Soup", calories: 300, ingredients: ["Chicken", "Carrot", "Potato"])
        ]
        completion(recipes, nil)
    }
}

// Пример использования Protected Variations
let userPreferencesService = UserPreferencesService()
let recipeService = RecipeService()

userPreferencesService.fetchData(id: 123) { preferences, error in
    if let preferences = preferences {
        print("User Preferences: \(preferences)")
    } else if let error = error {
        print("Error: \(error.localizedDescription)")
    }
}

recipeService.fetchData(id: 123) { recipes, error in
    if let recipes = recipes {
        print("Recipes: \(recipes)")
    } else if let error = error {
        print("Error: \(error.localizedDescription)")
    }
}
```
