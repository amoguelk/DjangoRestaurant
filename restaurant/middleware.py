class PrintRequest:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        print("\n🪲 User request:", request,"🪲\n")
        return self.get_response(request)
