from constants.tech_stack import TechStack
from constants.programming_language import ProgrammingLanguage

PROGRAMMING_LANGUAGE_TO_TECH_STACKS = {
  ProgrammingLanguage.JAVASCRIPT.value: [
    TechStack.REACTJS.value,
    TechStack.ANGULARJS.value,
    TechStack.VUEJS.value,
    TechStack.REMIX.value,
    TechStack.NEXTJS.value,
    TechStack.ASTRO.value,
    TechStack.NUXJS.value,
    TechStack.NESTJS.value,
    TechStack.EXPRESSJS.value,
    TechStack.ELECTRON.value,
    TechStack.REACT_NATIVE.value
  ],
  ProgrammingLanguage.PYTHON.value: [
    TechStack.DJANGO.value,
    TechStack.FLASK.value,
    TechStack.PANDAS.value,
    TechStack.NUMPY.value,
    TechStack.SCIPY.value,
    TechStack.TENSORFLOW.value,
    TechStack.PYTORCH.value,
    TechStack.SCIKIT_LEARN.value,
  ],
  ProgrammingLanguage.RUBY.value: [
    TechStack.RUBY_ON_RAILS.value,
    TechStack.SINATRA.value,
  ],
  ProgrammingLanguage.DART.value: [
    TechStack.AQUEDUCT.value,
    TechStack.FLUTTER.value,
  ],
  ProgrammingLanguage.SWIFT.value: [
    TechStack.VAPOR.value,
    TechStack.NATIVE_IOS.value,
  ],
  ProgrammingLanguage.KOTLIN.value: [
    TechStack.KTOR.value,
    TechStack.NATIVE_ANDROID.value
  ],
  ProgrammingLanguage.GO.value: [
    TechStack.GIN.value,
    TechStack.ECHO.value,
  ],
  ProgrammingLanguage.CSHARP.value: [
    TechStack.DOTNET.value,
    TechStack.ASPNET_CORE.value,
    TechStack.UNITY.value
  ],
  ProgrammingLanguage.CPP.value: [
    TechStack.WXWIDGETS.value,
    TechStack.UNREAL_ENGINE.value
  ],
}
