#  LLM Context Setting Repoisitory - Public Version

## Purpose Statement

The purpose of this repository is to demonstrate a small aggregation of contextual data about an individual (specifically me!) for evaluation as a seeding source of contextual data in experimenting with different approaches to RAG and context-setting in the much smaller personal implementation use case.

The LLM code generated folder is a transcript of an experiment that I tried using a large language model to conduct a context setting interview in which I instructed it to ask me questions and then gather them into specific themes intended to generate these context snippets.

These files, which I call context snippets, are simply small textual files, usually markdown, containing contextual pieces of data about a common subject. The intention is to consolidate them into vector storage through a data pipeline.

## LLM Assistants For Creating "Context Snippets"

I've developed some LLM assistants expressly for the purpose of helping to create these context snippets from text formatted more naturally, such as in large blocks of text or in dictated format. 

This tool is an assistant which helps the user to identify specific pieces of context data to set for this purpose. 

https://huggingface.co/chat/assistant/6762d5b9bb93201f4b42bcbd

This utility attempts to isolate contextual data from the surrounding text. 

https://huggingface.co/chat/assistant/6769775b53155b6690e86d5c

This utility is specifically intended to generate these contact snippets from dictated text, which is useful as it's a quite natural way of creating this information. 

https://huggingface.co/chat/assistant/6768d07954c6d31d32d3786e

This assistant serves much the same purpose, but is configured to be a little bit broader. It has in its configuration the ability to conduct these context setting interviews with the user if that is the chosen direction for the interaction. 

https://huggingface.co/chat/assistant/67624b04c43bc16e05331a06

## Use Case Statement

## Author

Daniel Rosehill  
(public at danielrosehill dot com)

## Licensing

This repository is licensed under CC-BY-4.0 (Attribution 4.0 International) 
[License](https://creativecommons.org/licenses/by/4.0/)

### Summary of the License
The Creative Commons Attribution 4.0 International (CC BY 4.0) license allows others to:
- **Share**: Copy and redistribute the material in any medium or format.
- **Adapt**: Remix, transform, and build upon the material for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the license terms.

#### License Terms
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **No additional restrictions**: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For the full legal code, please visit the [Creative Commons website](https://creativecommons.org/licenses/by/4.0/legalcode).