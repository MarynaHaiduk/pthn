def concat_args(*args, sep="/"):
    return sep.join(args)


print(concat_args("ab", "cd", "ef", "gh"))
