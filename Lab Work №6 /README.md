
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
