# 🤖 PocketGenie - AI Features Testing Guide

Complete guide to test all AI features in the PocketGenie mobile app.

---

## 📱 What's New

A new **AI Features Testing Screen** has been added to the mobile app with two tabs:

1. **Summarize Tab** - Test AI content summarization
2. **Prioritize Tab** - Test AI task prioritization

---

## 🚀 How to Access AI Features

### From Home Screen
1. Open the app
2. Look at the top AppBar (header)
3. Tap the **✨ (sparkle/auto_awesome)** icon
4. You'll see the AI Features Testing screen

### Alternative Navigation
- From any screen, you can navigate to `/ai-features` route

---

## 🧪 Feature 1: AI Content Summarization

### What It Does
The AI analyzes any text you provide and creates:
- A concise summary paragraph
- Key bullet points (up to 10)

### How to Test

**Step 1: Enter Text**
1. Go to the **Summarize** tab
2. Paste or type text in the text field
3. Example text to try:
   ```
   Project Management is the practice of initiating, planning, executing, 
   controlling, and closing the work of a team to achieve specific goals 
   and meet specific success criteria at the specified time. The primary 
   challenge of project management is to achieve all of the project goals 
   and objectives while honoring the preconceived constraints. The main 
   constraints are scope, time, quality, and budget.
   ```

**Step 2: Summarize**
1. Tap the **Summarize** button
2. Wait for the AI to process (2-5 seconds)
3. View the result in the green success card

**Step 3: Verify Results**
- ✅ Summary paragraph appears
- ✅ Bullet points are generated
- ✅ Key information is captured

### Expected Output
```
Summary: Project management involves initiating, planning, executing, 
controlling, and closing work to achieve specific goals. The main 
challenges include managing scope, time, quality, and budget constraints.

Bullet Points:
- Project management is the practice of coordinating team work
- Primary goal is achieving project objectives within constraints
- Main constraints are scope, time, quality, and budget
- Success requires meeting preconceived criteria
- Effective management balances all constraint factors
```

### Troubleshooting

**Issue: "Error: Connection refused"**
- Backend is not running
- Solution: Start backend with `docker-compose up -d`

**Issue: "Error: Request timeout"**
- Z.ai server is not responding
- Solution: Check backend logs with `docker-compose logs backend`

**Issue: Empty result**
- Text might be too short
- Solution: Try with longer text (at least 50 words)

---

## 🎯 Feature 2: AI Task Prioritization

### What It Does
The AI analyzes all your tasks and:
- Ranks them by urgency and importance
- Recommends the "Next Best Action"
- Provides reasoning for the prioritization

### How to Test

**Step 1: Create Test Tasks**
1. Go to **Tasks** tab
2. Create at least 3 tasks with different priorities:
   - Task 1: "Buy groceries" - Priority: Low
   - Task 2: "Finish project report" - Priority: High, Due: Tomorrow
   - Task 3: "Call client" - Priority: Urgent, Due: Today
   - Task 4: "Review code" - Priority: Medium

**Step 2: Access Prioritization**
1. Go to **AI Features** screen
2. Tap the **Prioritize** tab
3. You'll see your tasks listed

**Step 3: Run Prioritization**
1. Tap the **Prioritize Tasks** button
2. Wait for AI analysis (2-5 seconds)
3. View results in the green success card

**Step 4: Analyze Results**

The result shows:

**A. Next Best Action** (highlighted in amber)
- The single most important task to focus on
- Based on urgency, due date, and priority

**B. AI Reasoning**
- Explanation of how tasks were prioritized
- Considers due dates, priority levels, and urgency

**C. Prioritized Order**
- Numbered list of tasks in recommended order
- Shows due dates for each task

### Expected Output Example

```
Next Best Action:
⭐ Call client
   (Priority: Urgent, Due: Today)

AI Reasoning:
The task "Call client" has been prioritized as the next best action 
because it has an urgent priority level and is due today. This task 
should be completed immediately to avoid missing the deadline.

Prioritized Order:
1. Call client (Due: Today)
2. Finish project report (Due: Tomorrow)
3. Review code (No due date)
4. Buy groceries (No due date)
```

### Testing Scenarios

**Scenario 1: All tasks have same priority**
- Create 3 tasks with same priority
- AI will sort by due date
- Tasks with earlier due dates rank higher

**Scenario 2: Mix of urgent and low priority**
- Create mix of urgent and low priority tasks
- AI should recommend urgent tasks first
- Verify "Next Best Action" is urgent

**Scenario 3: No due dates**
- Create tasks without due dates
- AI will prioritize by priority level
- Verify sorting is correct

**Scenario 4: Complex scenario**
- Create 5+ tasks with various priorities and due dates
- AI should handle complex prioritization
- Verify reasoning makes sense

---

## 📊 Testing Checklist

### Summarization Feature
- [ ] Can enter text in the text field
- [ ] Summarize button works
- [ ] Loading indicator appears while processing
- [ ] Summary result displays correctly
- [ ] Bullet points are generated
- [ ] Error handling works (try with empty text)
- [ ] Can copy result text (SelectableText)

### Prioritization Feature
- [ ] Tasks are displayed correctly
- [ ] Prioritize button works
- [ ] Loading indicator appears while processing
- [ ] Next Best Action is highlighted
- [ ] AI Reasoning is displayed
- [ ] Prioritized order is numbered
- [ ] Error handling works (try with no tasks)
- [ ] Results are accurate based on task properties

### UI/UX
- [ ] Tabs switch smoothly
- [ ] Information cards are clear
- [ ] Icons are appropriate
- [ ] Colors are consistent
- [ ] Text is readable
- [ ] Buttons are responsive
- [ ] Loading states are clear

---

## 🔧 Advanced Testing

### Test with Different Content Types

**For Summarization:**
1. Technical documentation
2. Meeting notes
3. Email content
4. News articles
5. Long-form text

**For Prioritization:**
1. Work-related tasks
2. Personal tasks
3. Mixed priorities
4. Tasks with/without due dates
5. Completed vs incomplete tasks

### Performance Testing

Monitor these metrics:

| Metric | Expected | How to Check |
|--------|----------|-------------|
| Summarize time | <5 seconds | Use device timer |
| Prioritize time | <5 seconds | Use device timer |
| Memory usage | <150MB | Device settings |
| UI responsiveness | Smooth | Tap buttons quickly |

### Error Scenarios

Test these error cases:

1. **No internet connection**
   - Disable WiFi/mobile data
   - Try to summarize/prioritize
   - Should show error message

2. **Backend offline**
   - Stop backend: `docker-compose down`
   - Try to summarize/prioritize
   - Should show connection error

3. **Invalid input**
   - Empty text for summarization
   - No tasks for prioritization
   - Should show helpful error

4. **Timeout**
   - Very long text (>10,000 words)
   - Many tasks (>50)
   - Should handle gracefully

---

## 📈 Expected Behavior

### Summarization
- ✅ Accepts any text input
- ✅ Generates 1-10 bullet points
- ✅ Creates concise summary
- ✅ Preserves key information
- ✅ Handles long text
- ✅ Shows loading state
- ✅ Displays errors clearly

### Prioritization
- ✅ Analyzes all tasks
- ✅ Recommends next best action
- ✅ Provides reasoning
- ✅ Sorts by urgency
- ✅ Considers due dates
- ✅ Respects priority levels
- ✅ Shows loading state
- ✅ Displays errors clearly

---

## 🎯 Success Criteria

You've successfully tested AI features when:

✅ Summarization produces meaningful summaries
✅ Prioritization recommends logical task order
✅ Both features handle errors gracefully
✅ UI is responsive and clear
✅ Results are accurate and useful
✅ Loading states are visible
✅ No crashes or exceptions

---

## 📞 Troubleshooting

### Common Issues

**Issue: "No tasks to prioritize"**
- Solution: Create at least one task first

**Issue: "Please enter text to summarize"**
- Solution: Enter text in the text field

**Issue: Results not showing**
- Solution: Check backend is running and accessible

**Issue: Slow response**
- Solution: Check network connection and backend performance

**Issue: Incorrect prioritization**
- Solution: Verify task priorities and due dates are set correctly

---

## 🚀 Next Steps

After testing AI features:

1. **Report Issues**: Create GitHub issues for any bugs
2. **Suggest Improvements**: Add feature requests
3. **Explore Code**: Review `ai_features_screen.dart`
4. **Integrate Further**: Add AI features to other screens
5. **Customize**: Modify prompts and logic for your needs

---

## 📚 Related Files

- **Screen**: `mobile/lib/screens/ai_features_screen.dart`
- **Router**: `mobile/lib/config/router.dart`
- **API Service**: `mobile/lib/services/api_service.dart`
- **Backend API**: `backend/app/api/ai.py`
- **AI Service**: `backend/app/services/ai_service.py`

---

## 🎉 Tips for Best Results

1. **For Summarization:**
   - Use well-structured text
   - Include key information in the text
   - Try different text lengths
   - Test with various topics

2. **For Prioritization:**
   - Create tasks with different priorities
   - Set due dates for some tasks
   - Mix urgent and low-priority tasks
   - Test with 3-10 tasks

3. **General:**
   - Keep backend running
   - Check network connection
   - Monitor performance
   - Report any issues

---

## 📖 API Reference

### Summarize Endpoint
```
POST /ai/summarize
Content-Type: application/json

{
  "content": "Text to summarize...",
  "max_points": 5
}

Response:
{
  "summary": "Summary paragraph...",
  "bullet_points": ["Point 1", "Point 2", ...]
}
```

### Prioritize Endpoint
```
POST /ai/prioritize
Content-Type: application/json

{
  "tasks": [
    {
      "id": "uuid",
      "title": "Task title",
      "priority": 2,
      "due_date": "2024-01-15T10:00:00Z",
      ...
    }
  ]
}

Response:
{
  "prioritized_tasks": [...],
  "next_best_action": {...},
  "reasoning": "AI reasoning..."
}
```

---

**Happy testing! 🚀**

For more information, see [MOBILE_TESTING_GUIDE.md](./MOBILE_TESTING_GUIDE.md)

