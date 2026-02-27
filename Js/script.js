@RestController
public class QuestionController {
    
    @GetMapping("/questions")
    public List<Question> getQuestions() {
        return questionRepository.findAll();
    }

    @PostMapping("/ask")
    public Question addQuestion(@RequestBody Question q) {
        return questionRepository.save(q);
    }
}
