
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
User — интерфейс всех пользователей.

AdminUser и RegularUser — конкретные классы пользователей, которые реализуют интерфейс User.

UserFactory — интерфейс для фабрики, который создаёт пользователей.

AdminUserFactory и RegularUserFactory — фабрики, которые создают соответствующих пользователей.

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
UserPreferences и Menu — интерфейсы для предпочтений и меню.

VeganPreferences, RegularPreferences, VeganMenu, RegularMenu — конкретные классы для каждого типа пользователя.

UserEquipmentFactory — интерфейс для фабрики, которая создаёт соответствующие предпочтения и меню.

VeganUserFactory и RegularUserFactory — конкретные фабрики, создающие веганские и обычные объекты.

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

Пример:
Предположим, у нас есть класс AuthorizationManager, который управляет авторизацией пользователей. Мы хотим гарантировать, что в системе будет только один экземпляр этого класса.

Для этого создаём статическую переменную shared, которая будет хранить единственный экземпляр класса.
Инициализатор класса приватный, чтобы другие объекты не могли создать новый экземпляр.
Мы используем статический метод shared, чтобы получить доступ к этому экземпляру.

Пояснение:
Паттерн Одиночка решает проблему создания единственного объекта, например, для управления настройками, авторизацией или логированием в приложении. Использование этого паттерна гарантирует, что в любой момент времени будет только один экземпляр класса, что упрощает управление состоянием.

UML диаграмма:

AuthorizationManager — класс с единственным экземпляром (через статическую переменную shared).

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

Пример: Интеграция с внешним API для рецептов
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

Пример: Рекомендации на основе различных факторов (бюджет, диетические предпочтения)
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

Пример: Фильтрация рецептов по аллергии
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

Пример: Меню, состоящее из разных рецептов
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
Определяет семейство алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми. Позволяет изменять алгоритмы независимо от клиентов, которые ими пользуются.

Пример:
Клиент выполняет одно действие, но с разными классами одного интерфейса.

![image](https://github.com/user-attachments/assets/5b1284c2-14ee-434e-ad47-8fd8076188ed)

Код:
```Swift
protocol NavigationStrategy {
    func navigate()
}

class WalkingStrategy: NavigationStrategy {
    func navigate() {
        print("Используется стратегия пешеходной навигации")
    }
}

class CyclingStrategy: NavigationStrategy {
    func navigate() {
        print("Используется стратегия велосипедной навигации")
    }
}

class DrivingStrategy: NavigationStrategy {
    func navigate() {
        print("Используется стратегия автомобильной навигации")
    }
}

class Navigator {
    var navigationStrategy: NavigationStrategy

    init(navigationStrategy: NavigationStrategy) {
        self.navigationStrategy = navigationStrategy
    }

    func setNavigationStrategy(strategy: NavigationStrategy) {
        navigationStrategy = strategy
    }

    func navigate() {
        navigationStrategy.navigate()
    }
}
```
