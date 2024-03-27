# Andrew did this for me

from aiconfig import AIConfigRuntime, InferenceOptions
import asyncio

config = AIConfigRuntime.load("health.aiconfig.yaml")

inference_options = InferenceOptions(stream=True)

async def main():
  print("What can I help you with today?")
  question = input()
  context = "Top Questions About Fitness and Women Being physically active is one of the most important steps you can take to get and stay healthy. Women of all ages, shapes, and abilities benefit from getting active. Regular physical activity (exercise) can help lower your risk for many diseases that affect women, including heart disease and stroke. Exercise can also help relieve symptoms of some conditions, such as depression, type 2 diabetes, and high blood pressure. Women need to do different types of physical activities to reach or stay at a healthy weight and build strength and endurance. Q: How can physical activity help my health? A: Getting regular physical activity is one of the best things you can do for your health. Regular physical activity can help: • Lower blood pressure and cholesterol • Improve depression • Improve sleep • Lower your risk of diseases such as breast cancer, colon cancer, type 2 diabetes, heart disease, and stroke • Lower your risk of dying early Q: How much physical activity should I do? A: Each week, women should get at least: • 2 hours and 30 minutes (150 minutes) of moderate-intensity aerobic physical activity. You know you are doing a moderate-intensity activity OR • 1 hour and 15 minutes (75 minutes) of vigorousintensity aerobic activity. You know you are doing a vigorous-intensity physical activity when you are breathing hard and it is difficult to have a conversation. This could be a 40-minute jog or step class twice a week. AND • Muscle-strengthening activities on two or more days. Q: Can I exercise if I have underweight, overweight, or obesity? A: Maybe. People who are underweight due to an eating disorder should not exercise unless their doctor tells them to. Women who have overweight or obesity should talk to their doctor or nurse about any concerns they have about beginning an exercise program. For most people, any amount or type of physical activity will help your overall health. Physical activity can also improve muscle strength, balance, and flexibility. Start slowly if you haven’t been physically active before or if it has been a while. Talk to your doctor or nurse about exercise if you have a health condition. Your doctor or nurse can help you develop an exercise plan that is healthy and safe for a person of your current weight and fitness level. Q: Can exercise help menstrual cramps? A: Maybe. Researchers have found that some women have fewer painful cramps during menstruation if they when your heart is beating faster but you can still exercise regularly. There are almost no risks to regular physical activity, like walking, which may also help you feel better during your period. Q: Is it safe to exercise during pregnancy? A: Physical activity during pregnancy is usually safe and healthy for you and your baby. And the more active you are during pregnancy, the easier it will be to start getting active after your baby is born. Talk to your doctor about your activity level throughout your pregnancy. Q: How can I avoid weight gain after menopause? A: As you age, and especially in the years after menopause, you may find it harder to maintain your weight. You may need to increase the amount of physical activity you get and lower how many calories you eat to stay the same weight. carry on a conversation. Try a brisk, 30-minute walk five times a week.  Q: How can physical activity help older women? A: As you get older, regular physical activity helps: • Keep bones strong • Prevent hip fractures (breaking your hip) • Decrease pain from arthritis • Prevent dementia • Maintain your independence Balance exercises are important for all women, but especially older women who are at a higher risk of falls. Examples of these exercises include tai chi and standing from a sitting position.  Citation: Top Questions About Fitness and Women, https://owh-wh-d9-dev.s3.amazonaws.com/s3fs-public/documents/fact-sheet-fitness-and-women.pdf"
  print("thinking...")
  await config.run("health-question", params = {"question" : question, "context": context}, options=inference_options)
  print("done")

if __name__=="__main__":
  asyncio.run(main())