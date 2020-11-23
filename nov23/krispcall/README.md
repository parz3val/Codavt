# VOIP Research

VOIP is the transmission of multimedia over the IP network

VOIP Pipeline:

Client 1 (PSTN) <--> PSTN Network (SS7) <--> IP Telephony provider (SIP) <--> Routing Server <--> Client 2 (HTTP)

Twilio VOIP pipeline with Twilio tools:
Client 1 (Twilio Flex) --> Twilio Server --> Client 2 (Twilio Flex)

Twilio VOIP pipeline with helper library:
Client 1 (HTTP) --> Twilio Server(HTTP, TWiML) --> Routing platform/server --> Client 2 (HTTP)

Twilio VOIP pipeline with elastic SIP:
Clients (PSTN /HTTP) --> Twilio Server (HTTP) --> SIP server or agents (SIP) <--> Platform(HTTP)

## Possible feature sets

- Call
- SMS
- Call forwarding and routing
- Automatic attendants
- Phone number types
- Extensions
- Blocking and auto rejections
- Voicemail to text
- Call recording
- Call history
- Instant responding
- Custom greetings

## Software (Application Layer) Requirements and architecture

- Voice Over Internet Protocol - Transfers multimedia between over IP
- Session Initiation Protocol (SIP) - Creates a multimedia session between two API endpoints

To send the data over the IP network to PSTN or LTE network, we need SS7 servers with the SIP functionality (more: `https://www.patton.com/whitepapers/intro_to_ss7_tutorial.pdf`), access to SS7 Network, SIP communication systems.

The current fashion in development is in abstraction of the communication systems and separation of the hardware/networking complexity from the software engineering.

## Options for creating a PSTN ->

Twilio is the most popular communication system infrastructure provider.Twilio abstracts away the networking, routing, and signaling complexities involved in traditional LTE/PSTN networks and provides a set of predefined endpoints/featuresets to write telphony apps.

### Twilio Feature sets

- Use case API : set of APIs to solve comms problems in SE

  - Authy : provides the authenticaion features using phonenumber
  - TaskRouter : routes actions and manages services
  - Notify : gPRC service, can be used to make stuff like Viber, Whatsapp and stuff or send notifications like google messaging service

- Comms API

  - Voice
  - Lookup : Check the carrier, and details of the phone number
  - SMS and MMS
  - Phone number : uuid class to identify entities and processes, can be assigned to programs or individuals
    - Omni channel routing : Two way routing to/from VoLTE/IP
    - acc alerts
    - arrival alerts
    - service alerts
    - phone verification : verify phonenumbers kinda like HLR system
    - call marketing
    - webrtc gateway : can be used to route data/calls to the devices on network
    - lead alerts
    - IVR/ phone tree : Interactive phone response, like recharge and data taking systems and stuff
    - Masked phone numbers
    - CRM dialer
    - Conference call
    - Elastic SIP truncking
    - 2FA

- Progammable connectivity

### Twilio Limits

- Sending and Receiving Limitations on Calls and SMS

  - 1 CPS per account, each twillio project can make about 1 Call per second

  - 1 Message segment per second

  - Twilio conference call has max limit of 250

  - API request queuing:
    When Twilio receives message from our application, these requests are queued for delivery in the order we receive them. Each of our Twilio phone numbers has a separate queue, and each queue can hold up to 4 hours' worth of message segments based on the sending rate for a phone number type. For example, a local phone number from the US or Canada has a full queue of 14,400 message segments.

- Known issues and limits

  - There's an issue when viewing/searching for SMS transaction logs. When you search for the logs using phone number as a search tool, sometimes the results will not show up.

  - Errors from dialer aren't added to the Twillio debugger; are only sent to the Agent UI in twillio, so it can be headache to handle errors from the API. Though not as reliable or perfect, default client has some error codes. If the user is already connected, the call will fail with `SIP 486 Busy here.` More codes: `https://www.twilio.com/docs/api/errors`

### Telasip : `https://www.telasip.com/`

### VOIP.ms : `https://voip.ms/`

> > Note: Understand the difference between Telphony systems and PBX systems. PBX is a internal networking of IP voice devices, telphony systems connect to the PSTN network. PBX systems provide high level control like intranet,ip phones, creating and assigning new numbers, SIP truncking and routing, tracerouting and more.
> > Simple telphony systems only provide outgoing and incoming connection streams to the existing addresses/phone numbers.
