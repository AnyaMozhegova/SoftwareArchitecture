**UML:** 
```PlantUML
@startuml
interface User {
  + register(): void
}

class AdminUser implements User {
  + register(): void
}

class RegularUser implements User {
  + register(): void
}

interface UserFactory {
  + createUser(): User
}

class AdminUserFactory implements UserFactory {
  + createUser(): User
}

class RegularUserFactory implements UserFactory {
  + createUser(): User
}

UserFactory <|.. AdminUserFactory
UserFactory <|.. RegularUserFactory
User <|.. AdminUser
User <|.. RegularUser
AdminUserFactory --> AdminUser
RegularUserFactory --> RegularUser

@enduml
```

**UML:** 
```PlantUML
@startuml
interface UserPreferences {
  + setPreferences(): void
}

interface Menu {
  + createMenu(): void
}

class VeganPreferences implements UserPreferences {
  + setPreferences(): void
}

class RegularPreferences implements UserPreferences {
  + setPreferences(): void
}

class VeganMenu implements Menu {
  + createMenu(): void
}

class RegularMenu implements Menu {
  + createMenu(): void
}

interface UserEquipmentFactory {
  + createPreferences(): UserPreferences
  + createMenu(): Menu
}

class VeganUserFactory implements UserEquipmentFactory {
  + createPreferences(): VeganPreferences
  + createMenu(): VeganMenu
}

class RegularUserFactory implements UserEquipmentFactory {
  + createPreferences(): RegularPreferences
  + createMenu(): RegularMenu
}

UserEquipmentFactory <|.. VeganUserFactory
UserEquipmentFactory <|.. RegularUserFactory
UserPreferences <|.. VeganPreferences
UserPreferences <|.. RegularPreferences
Menu <|.. VeganMenu
Menu <|.. RegularMenu

@enduml
```

**UML:** 
```PlantUML
@startuml
class AuthorizationManager {
  - shared: AuthorizationManager
  - constructor(): void
  + authorizeUser(): void
  + getSharedInstance(): AuthorizationManager
}

AuthorizationManager --> AuthorizationManager : shared
@enduml

```
