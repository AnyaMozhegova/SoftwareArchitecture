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
```PlantUML
@startuml
class ExternalRecipeAPI {
    + getRecipesFromAPI(): [String] 
}

class RecipeService {
    + fetchRecipes(completion: @escaping ([Recipe]?, Error?) -> Void)
}

class RecipeServiceAdapter {
    - externalAPI: ExternalRecipeAPI
    + init(externalAPI: ExternalRecipeAPI)
    + fetchRecipes(completion: @escaping ([Recipe]?, Error?) -> Void)
}

ExternalRecipeAPI --|> RecipeServiceAdapter : «use»
RecipeServiceAdapter --|> RecipeService : «inherit»
@enduml

```

```PlantUML
@startuml
class Recommendation {
    + generateRecommendations(): [Recipe]
}

class BudgetRecommendation {
    + generateRecommendations(): [Recipe]
}

class DietaryRecommendation {
    + generateRecommendations(): [Recipe]
}

Recommendation <|-- BudgetRecommendation
Recommendation <|-- DietaryRecommendation
@enduml
```
```PlantUML
@startuml
class RecipeProvider {
    + getRecipes(): [Recipe]
}

class SimpleRecipeProvider {
    + getRecipes(): [Recipe]
}

class AllergyFilterDecorator {
    - decoratedProvider: RecipeProvider
    + init(decoratedProvider: RecipeProvider)
    + getRecipes(): [Recipe]
}

SimpleRecipeProvider --|> RecipeProvider
AllergyFilterDecorator --|> RecipeProvider
AllergyFilterDecorator *-- SimpleRecipeProvider : «has»
@enduml
```
```PlantUML
@startuml
class MenuItem {
    + getDescription(): String
}

class RecipeMenuItem {
    + getDescription(): String
}

class MenuCollection {
    + addItem(item: MenuItem)
    + getDescription(): String
}

RecipeMenuItem --|> MenuItem
MenuCollection --|> MenuItem
MenuCollection o-- RecipeMenuItem : «contains»
@enduml
```

```PlantUML
@startuml
interface NavigationStrategy {
    + navigate(): void
}

class WalkingStrategy {
    + navigate(): void
}

class CyclingStrategy {
    + navigate(): void
}

class DrivingStrategy {
    + navigate(): void
}

class Navigator {
    - navigationStrategy: NavigationStrategy
    + setNavigationStrategy(strategy: NavigationStrategy): void
    + navigate(): void
}

Navigator --|> NavigationStrategy
Navigator *-down-> WalkingStrategy: strategy
Navigator *-down-> CyclingStrategy: strategy
Navigator *-down-> DrivingStrategy: strategy
@enduml
```
