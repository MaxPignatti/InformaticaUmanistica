package controller;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@RestController
@RequestMapping("/api")
public class ApiController {

    @PostMapping("/sendText")
    public String sendText(@RequestBody String text) {
        System.out.println("Sending text: " + text);
        String url = "https://robomatic-ai.p.rapidapi.com/api";
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        headers.set("X-RapidAPI-Key", "SIGN-UP-FOR-KEY");
        headers.set("X-RapidAPI-Host", "robomatic-ai.p.rapidapi.com");
        String requestBody = "in=What's%202%20plus%205%3F&op=in&cbot=1&SessionID=RapidAPI1&cbid=1&key=RHMN5hnQ4wTYZBGCF3dfxzypt68rVP&ChatSource=RapidAPI&duration=1";
        HttpEntity<String> entity = new HttpEntity<>(requestBody, headers);

        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> responseEntity = restTemplate.postForEntity(url, entity, String.class);

        String response = responseEntity.getBody();
        System.out.println(response);

        return "OK";
    }
}
