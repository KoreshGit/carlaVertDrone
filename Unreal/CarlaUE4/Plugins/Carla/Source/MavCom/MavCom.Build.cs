// Copyright 1998-2017 Epic Games, Inc. All Rights Reserved.
using UnrealBuildTool;
using System;
using System.IO;

public class MavCom : ModuleRules
{
  
  public MavCom(ReadOnlyTargetRules Target) : base(Target)
  {

   
    bEnableExceptions = true;

    PrivatePCHHeaderFile = "Private/MavComPrivatePCH.h";
    
    PrivateDependencyModuleNames.AddRange(new string[] {"Core", "CoreUObject", "Engine"}); 
    CppStandard = CppStandardVersion.Cpp17;
    PublicSystemIncludePaths.Add("/home/kore/install2/include/mavsdk"); 
    PublicSystemLibraryPaths.Add("/home/kore/MAVSDK/install/lib");
    //PublicSystemLibraryPaths.Add("/home/kore/MAVSDK/build/default/third_party/install/lib");
    
 PublicSystemLibraryPaths.Add("/lib/x86_64-linux-gnu");

//PublicAdditionalLibraries.Add("stdc++");
 PublicAdditionalLibraries.Add("pthread");
/*     PublicAdditionalLibraries.Add("m");
    PublicAdditionalLibraries.Add("curl");
    PublicAdditionalLibraries.Add("jsoncpp");
    PublicAdditionalLibraries.Add("tinyxml2");
    PublicAdditionalLibraries.Add("z");
    PublicAdditionalLibraries.Add("ckore"); */
   // PublicAdditionalLibraries.Add("/usr/lib/gcc/x86_64-linux-gnu/9/libstdc++.so");
    PublicAdditionalLibraries.Add("mavsdk");


    

  RuntimeDependencies.Add("mavsdk");
 
 //PublicDelayLoadDLLs.Add("/home/kore/MAVSDK/install/lib")
   
    //PublicLibraryPaths.Add("/home/kore/MAVSDK/build/src/mavsdk");
   

/*  PublicSystemIncludePaths.Add("/home/kore/libtest");

 PublicSystemLibraryPaths.Add("/home/kore/libtest");
 PublicAdditionalLibraries.Add("mylib");
 */
}
}
